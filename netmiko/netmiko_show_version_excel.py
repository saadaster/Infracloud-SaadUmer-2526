from netmiko import ConnectHandler
from openpyxl import Workbook
import re

# === 1. Define router connection details ===
router = {
    "device_type": "cisco_ios",
    "ip": "192.168.56.101",      # Replace with your router's IP
    "username": "cisco",       # Replace with your SSH username
    "password": "cisco123!",       # Replace with your SSH password
}

# === 2. Connect to the router ===
print("Connecting to the router...")
connection = ConnectHandler(**router)

# === 3. Run commands to gather information ===
output = connection.send_command("show version")

# === 4. Extract useful info ===
# Example parsing (works for Cisco IOS-style output)
hostname_match = re.search(r"(\S+)\suptime", output)
version_match = re.search(r"Version\s+([\S]+)", output)
model_match = re.search(r"[Cc]isco\s+(\S+)\s+\(revision", output)
serial_match = re.search(r"System serial number\s+:\s+(\S+)", output)

hostname = hostname_match.group(1) if hostname_match else "Unknown"
version = version_match.group(1) if version_match else "Unknown"
model = model_match.group(1) if model_match else "Unknown"
serial = serial_match.group(1) if serial_match else "Unknown"

# === 5. Save data into Excel ===
wb = Workbook()
ws = wb.active
ws.title = "Router Info"

# Headers
headers = ["Hostname", "Version", "Model", "Serial Number", "IP Address"]
ws.append(headers)

# Data row
ws.append([hostname, version, model, serial, router["ip"]])

# Save the Excel file
file_name = "router_info.xlsx"
wb.save(file_name)

print(f"\n✅ Router info saved to '{file_name}' successfully!")

# === 6. Close connection ===
connection.disconnect()
