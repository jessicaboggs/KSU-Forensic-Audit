import requests
import sys

# TARGET: The specific KSU report URLs that are failing
TARGET_URLS = [
    "https://kysu.edu",
    # Add other suspect URLs here
]

def check_transparency_fail(url):
    print(f"[*] Auditing: {url}")
    
    try:
        # 1. Check Live Status (Allowing redirects to see where they dump us)
        response = requests.get(url, timeout=10)
        
        # Check for 302/301 Redirects specifically
        if response.history:
            print(f"    [!] REDIRECT DETECTED: {response.history[0].status_code}")
            print(f"    [>] Redirected to: {response.url}")
            
            # If it redirects to a generic homepage or unrelated page, flag it
            if "kysu.edu" in response.url and url not in response.url:
                print("    [X] SOFT 404 / DEFLECTION CONFIRMED")
        
        # Check for hard 404
        elif response.status_code == 404:
             print("    [X] HARD 404: Document Removed")
        
        elif response.status_code == 200:
             print("    [?] STATUS 200: Page exists (Verify content manually)")

    except requests.exceptions.RequestException as e:
        print(f"    [!] CONNECTION ERROR: {e}")

def check_wayback_availability(url):
    # Check if Wayback has it, or if KSU blocked crawling via robots.txt
    archive_api = f"http://archive.org{url}"
    try:
        r = requests.get(archive_api)
        data = r.json()
        
        if not data.get('archived_snapshots'):
             print("    [XX] WAYBACK BLOCK: No snapshots available (Suspicious for public entities)")
        else:
             last_save = data['archived_snapshots']['closest']['timestamp']
             print(f"    [i] Last Archived: {last_save}")
             
    except Exception as e:
        print(f"    [!] Archive Check Failed: {e}")

if __name__ == "__main__":
    print("--- KSU 1.1 TRANSPARENCY AUDIT ---")
    for url in TARGET_URLS:
        check_transparency_fail(url)
        check_wayback_availability(url)
        print("-" * 30)
