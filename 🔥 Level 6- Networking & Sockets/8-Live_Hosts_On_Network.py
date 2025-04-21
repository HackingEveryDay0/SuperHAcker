# 8.​ Implement a script that finds live hosts on a local network.

import asyncio
import socket
import struct
import subprocess
import platform
import fcntl  # Linux-specific for ioctl
import re

async def get_local_ip_and_mask():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))
        local_ip = s.getsockname()[0]
    except Exception as e:
        print(f"Error getting local IP: {e}")
        return None, None
    finally:
        s.close()

    subnet_mask = None
    if platform.system().lower() == 'linux':
        subnet_mask = get_subnet_mask_linux(local_ip)
    if not subnet_mask:
        subnet_mask = await get_subnet_mask_subprocess(local_ip)

    return local_ip, subnet_mask

def get_subnet_mask_linux(ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        interfaces = get_interfaces()
        for iface in interfaces:
            result = fcntl.ioctl(
                s.fileno(),
                0x891B,  # SIOCGIFNETMASK
                struct.pack('256s', iface.encode('utf-8'))
            )
            mask = socket.inet_ntoa(result[20:24])
            if ip.startswith('.'.join(mask.split('.')[:3])) or mask == '255.255.255.255':
                return mask
    except Exception:
        return None
    finally:
        s.close()
    return None

def get_interfaces():
    try:
        if platform.system().lower() == 'linux':
            output = subprocess.check_output(['ip', 'link']).decode('utf-8')
            interfaces = re.findall(r'\d+: (.*?):', output)
            return interfaces
        return []
    except subprocess.CalledProcessError:
        return []

async def get_subnet_mask_subprocess(ip):
    try:
        if platform.system().lower() == 'windows':
            process = await asyncio.create_subprocess_exec(
                'ipconfig',
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, _ = await process.communicate()
            output = stdout.decode('utf-8')
            lines = output.splitlines()
            for i, line in enumerate(lines):
                if ip in line:
                    for j in range(i, len(lines)):
                        if 'Subnet Mask' in lines[j]:
                            mask = lines[j].split(':')[-1].strip()
                            return mask
        else:
            process = await asyncio.create_subprocess_exec(
                'ip', 'addr',
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, _ = await process.communicate()
            output = stdout.decode('utf-8')
            for line in output.splitlines():
                if ip in line and 'inet' in line:
                    cidr = re.search(r'inet \S+/\d+', line)
                    if cidr:
                        prefix = int(cidr.group(0).split('/')[-1])
                        mask = prefix_to_netmask(prefix)
                        return mask
    except (subprocess.SubprocessError, asyncio.TimeoutError):
        pass
    return None

def prefix_to_netmask(prefix):
    mask = (0xffffffff << (32 - prefix)) & 0xffffffff
    return int_to_ip(mask)

def ip_to_int(ip):
    try:
        return struct.unpack("!I", socket.inet_aton(ip))[0]
    except socket.error:
        return None

def int_to_ip(int_ip):
    return socket.inet_ntoa(struct.pack("!I", int_ip))

def generate_subnet_ips(ip, subnet_mask):
    if not ip or not subnet_mask:
        print("Invalid IP or subnet mask.")
        return []

    ip_int = ip_to_int(ip)
    mask_int = ip_to_int(subnet_mask)
    if ip_int is None or mask_int is None:
        print("Error converting IP or subnet mask.")
        return []

    network_int = ip_int & mask_int
    broadcast_int = network_int | (~mask_int & 0xFFFFFFFF)

    num_hosts = broadcast_int - network_int + 1
    if num_hosts <= 2:
        print(f"Subnet {subnet_mask} has no usable host IPs.")
        return []

    if num_hosts > 1000:
        print(f"Warning: Subnet has {num_hosts-2} usable IPs, scanning may take time.")

    return [int_to_ip(i) for i in range(network_int + 1, broadcast_int)]

async def is_host_alive(ip, semaphore):
    async with semaphore:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', ip]
        process = None
        try:
            process = await asyncio.create_subprocess_exec(
                *command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            await asyncio.wait_for(process.communicate(), timeout=2)
            await process.wait()  # Ensure process is fully terminated
            return ip, process.returncode == 0
        except (asyncio.TimeoutError, subprocess.SubprocessError):
            return ip, False
        finally:
            if process is not None and process.returncode is None:
                try:
                    process.terminate()
                    await asyncio.wait_for(process.wait(), timeout=1)
                except asyncio.TimeoutError:
                    process.kill()  # Force kill if terminate fails
                    await process.wait()

def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except socket.herror:
        return None

async def main():
    local_ip, subnet_mask = await get_local_ip_and_mask()
    if not local_ip or not subnet_mask:
        print("Could not determine local IP or subnet mask. Assuming /24 as fallback.")
        local_ip = local_ip or "192.168.1.1"
        subnet_mask = "255.255.255.0"

    print(f"My IP Address: {local_ip}")
    print(f"Subnet Mask: {subnet_mask}")

    subnet_ips = generate_subnet_ips(local_ip, subnet_mask)
    if not subnet_ips:
        print("No usable IPs found in the subnet.")
        return

    print(f"Scanning {len(subnet_ips)} IP addresses for live hosts concurrently...")

    semaphore = asyncio.Semaphore(20)
    tasks = [is_host_alive(ip, semaphore) for ip in subnet_ips]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    live_hosts = []
    for ip, is_alive in results:
        if isinstance(is_alive, Exception):
            continue  # Skip tasks that raised exceptions
        if is_alive:
            hostname = get_hostname(ip)
            live_hosts.append((ip, hostname if hostname else "No hostname"))
            print(f"Live host found: {ip} (Hostname: {hostname if hostname else 'No hostname'})")

    print(f"\nFound {len(live_hosts)} live hosts:")
    for ip, hostname in live_hosts:
        print(f"IP: {ip}, Hostname: {hostname}")

if __name__ == "__main__":
    asyncio.run(main())