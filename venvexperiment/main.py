# main.py
import requests
import sys

# This checks where Python is running from
print(f"Running from: {sys.prefix}")

try:
    # Attempt to use the library we installed in the venv
    response = requests.get('https://api.ipify.org?format=json')
    ip = response.json()['ip']
    print(f"SUCCESS! Your IP is: {ip}")
    
except ModuleNotFoundError:
    print("FAILURE! The 'requests' library was not found.")