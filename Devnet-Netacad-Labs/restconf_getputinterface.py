import requests
requests.packages.urllib3.disable_warnings()

IP_HOST = "192.168.56.101"
RESTCONF_USERNAME = "cisco"
RESTCONF_PASSWORD = "cisco123!"
DATA_FORMAT = "application/yang-data+json"
LOOPBACK_INTERFACE = "Loopback11"
LOOPBACK_IP = "10.19.12.1"

api_url_put = f"https://{IP_HOST}/restconf/data/ietf-interfaces:interfaces/interface={LOOPBACK_INTERFACE}"
api_url_get = f"https://{IP_HOST}/restconf/data/ietf-interfaces:interfaces"
headers = {"Accept": DATA_FORMAT, "Content-type": DATA_FORMAT}
basicauth = (RESTCONF_USERNAME, RESTCONF_PASSWORD)

yangConfig = {
    "ietf-interfaces:interface": {
        "name": LOOPBACK_INTERFACE,
        "description": f"RESTCONF => {LOOPBACK_INTERFACE}",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": LOOPBACK_IP,
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

# PUT Request
print("=" * 50)
print("CREATING/UPDATING LOOPBACK INTERFACE")
print("=" * 50)
resp_put = requests.put(api_url_put, json=yangConfig, auth=basicauth, 
                        headers=headers, verify=False)

if resp_put.status_code in range(200, 300):
    print(f"✓ STATUS OK: {resp_put.status_code}")
else:
    print("✗ ERROR")
    print(f"Status Code: {resp_put.status_code}")
    print(resp_put.text)

# GET Request
print("\n" + "=" * 50)
print("RETRIEVING ALL INTERFACES")
print("=" * 50)
resp_get = requests.get(api_url_get, auth=basicauth, headers=headers, verify=False)

if resp_get.status_code == 200:
    print(f"✓ STATUS OK: {resp_get.status_code}")
    import json
    print("\nInterfaces Configuration:")
    print(json.dumps(resp_get.json(), indent=2))
else:
    print("✗ ERROR")
    print(f"Status Code: {resp_get.status_code}")
    print(resp_get.text)

# GET specific loopback interface
print("\n" + "=" * 50)
print(f"RETRIEVING {LOOPBACK_INTERFACE}")
print("=" * 50)
resp_get_loopback = requests.get(api_url_put, auth=basicauth, headers=headers, verify=False)

if resp_get_loopback.status_code == 200:
    print(f"✓ STATUS OK: {resp_get_loopback.status_code}")
    print("\nLoopback Configuration:")
    print(json.dumps(resp_get_loopback.json(), indent=2))
else:
    print("✗ ERROR")
    print(f"Status Code: {resp_get_loopback.status_code}")