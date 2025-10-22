import requests
import sys
from datetime import datetime

def main():
    url = "https://api.myip.com"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # check HTTP errors
    except requests.RequestException as e:
        print(f"Fout bij ophalen IP: {e}", file=sys.stderr)
        sys.exit(1)
    
    try:
        data = response.json()
        ip = data.get("ip", "unknown")
        country = data.get("country", "unknown")
        cc = data.get("cc", "unknown")
    except ValueError:
        print("Kon JSON niet parsen", file=sys.stderr)
        sys.exit(2)

    # Huidige tijd
    now = datetime.now()

    print(f"[{now}] IP: {ip}, Country: {country}, CC: {cc}")

if __name__ == "__main__":
    main()