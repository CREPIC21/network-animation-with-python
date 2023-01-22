from netmiko import ConnectHandler
import re

host_ip_address_pattern = re.compile("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
interface_pattern = re.compile("^(Ethernet|FastEthernet|GigabitEthernet|TenGigabitEthernet|Serial|Tunnel|Loopback|Vlan|BVI)[0-9/.]+$")

# asking for host IP to connect to
host_ip = input('Host IP to connect to: ')
if not host_ip_address_pattern.match(host_ip):
    print('Invalid IP address entered')
    exit(1)
# asking for which interface to check if it's shutdown
interface = input('Enter router interface to check if it is shutdown: ')
if not interface_pattern.match(interface):
    print('Invalid router interface entered, valid examples are: Ethernet0/1, GigabitEthernet0/1 ...')
    exit(1)
# asking for username to connect via SSH
username = input("Username: ")
# asking for password to connect via SSH
password = input('Enter password: ')
# creating a dictionary for the device to connect to
cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': host_ip,
       'username': username,
       'password': password,
       'port': 22,             # optional, default 22
       'secret': password,     # enable password
       'verbose': True         # optional, default False
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)

print(connection.find_prompt())

# getting the router configuration
output = connection.send_command(f'show interface {interface}')
# new_output = output.split('\n')
# print(output.split('\n')[0].rstrip().endswith('down'))
if output.split('\n')[0].rstrip().endswith('down'):
    commands = [f'interface {interface}', 'no shutdown', 'exit']
    print('Interface down')
    # entering the enabled mode on the device
    print('Entering enabled mode...')
    connection.enable()
    # entering config mode
    connection.config_mode()
    print('Entering config mode...')
    # sending commands to turn interface up
    connection.send_config_set(commands)
    print(f'Interface {interface} is up.')
else:
    print(f'Interface {interface} is alreday up')

# closing the connection
print('Closing connection')
connection.disconnect()

### IMPORTANT ###
"""
- GNS3 topology used: netmiko_scp
"""
