### DEVNET SANDBOX 
import datetime
print("Current date and time : ")
print(datetime.datetime.now())
print("Connecting via SSH => show version")

from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="CSR1kv",
    port="22",
    username="cisco",
    password="cisco123!"
    )
output=sshCli.send_command("show version")
print(output)