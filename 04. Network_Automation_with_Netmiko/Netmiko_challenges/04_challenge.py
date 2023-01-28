"""
Create a Python script that connects to a Cisco Router using SSH and Netmiko. The script should execute
the show ip int brief and show run commands.
Print out the output of each command.
"""

from netmiko import ConnectHandler

with open('./testing_text_files/router_info.txt') as f:
    info = f.readline().split(':')

# creating a dictionary for the device to connect to
cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': info[0],
       'username': info[2],
       'password': info[3],
       'port': info[1],             # optional, default 22
       'secret': info[4],      # this is the enable password
       'verbose': True         # optional, default False
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)

# entering the enabled mode on the device
connection.enable()

output_1 = connection.send_command('show ip int brief')
print(output_1)
print('#'*80)
output_2 = connection.send_command('show run')
print(output_2)

# closing the connection
print('Closing connection')
connection.disconnect()