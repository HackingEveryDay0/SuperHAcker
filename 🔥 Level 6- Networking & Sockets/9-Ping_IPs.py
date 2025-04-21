# 9.​ Write a program that pings a list of IPs and prints their status.

import subprocess
import platform
import time

def ping_ips(ip_list):
    # Determine ping command parameter based on OS
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    for ip in ip_list:
        try:
            # Run ping command (1 ping, 2-second timeout)
            result = subprocess.run(
                ['ping', param, '1', '-w', '2', ip],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if result.returncode == 0:
                # Extract response time from output (if available)
                output = result.stdout
                time_ms = "N/A"
                if "time=" in output:
                    try:
                        # Extract time from output (format varies by OS)
                        time_part = output.split("time=")[1].split()[0]
                        time_ms = time_part.replace("ms", "")
                    except:
                        pass
                print(f"{ip} is UP (Response time: {time_ms} ms)")
            else:
                print(f"{ip} is DOWN")
                
        except Exception as e:
            print(f"{ip} is DOWN (Error: {str(e)})")
            
        # Small delay to avoid overwhelming the network
        time.sleep(0.5)

def main():
    # Example list of IP addresses to ping
    ip_addresses = [
        "8.8.8.8",        # Google DNS
        "1.1.1.1",        # Cloudflare DNS
        "192.168.1.1",    # Common local router
        "10.0.0.1",       # Another common local IP
        "172.16.0.1",     # Private network IP
    ]
    
    print("Pinging IP addresses...\n")
    ping_ips(ip_addresses)

if __name__ == "__main__":
    main()