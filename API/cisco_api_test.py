import requests
import json
import urllib3

# 1. We negeren SSL-certificaat waarschuwingen (alleen voor demo/sandbox omgevingen!)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_interfaces():
    # De gegevens van de Cisco 'Always-On' Sandbox
    # Router: CSR1000v
    HOST = 'sandbox-iosxe-latest-1.cisco.com'
    PORT = '443'
    USER = 'developer'
    PASS = 'C1sco12345'

    # De URL voor RESTCONF (dit is het 'adres' van de interface-data)
    url = f"https://{HOST}:{PORT}/restconf/data/ietf-interfaces:interfaces"

    # Headers zijn cruciaal bij RESTCONF. We vertellen de router:
    # "Geef me de data terug in JSON formaat (niet XML)"
    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }

    print(f"Verbinding maken met {HOST}...")

    try:
        # 2. De daadwerkelijke API Call (GET request)
        response = requests.get(
            url, 
            auth=(USER, PASS), 
            headers=headers, 
            verify=False
        )

        # Check of de request gelukt is (Status code 200 = OK)
        if response.status_code == 200:
            print("Succes! Data ontvangen.\n")
            
            # 3. De ruwe JSON data omzetten naar een Python Dictionary
            api_data = response.json()

            # Laten we de data netjes printen
            interfaces = api_data['ietf-interfaces:interfaces']['interface']
            
            print(f"{'INTERFACE NAAM':<20} | {'BESCHRIJVING':<20} | {'STATUS'}")
            print("-" * 60)

            for iface in interfaces:
                name = iface.get('name')
                desc = iface.get('description', 'Geen beschrijving')
                enabled = iface.get('enabled')
                status = "UP" if enabled else "DOWN"

                print(f"{name:<20} | {desc:<20} | {status}")

        else:
            print(f"Oeps! Iets ging mis. Status code: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")

if __name__ == "__main__":
    get_interfaces()