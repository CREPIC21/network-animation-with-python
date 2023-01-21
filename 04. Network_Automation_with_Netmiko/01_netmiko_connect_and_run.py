
##### First way to connect to the device #####
"""
from netmiko import Netmiko

connection = Netmiko(host='192.168.122.4', port='22', username='admin', password='admin', device_type='cisco_ios')
output = connection.send_command('sh ip int brief')
print(output)

print('Closing connection')
connection.disconnect()
"""

##### Second way to connect to the device #####

from netmiko import ConnectHandler

# creating a dictionary for the device to connect to
cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '192.168.122.4',
       'username': 'admin',
       'password': 'admin',
       'port': 22,             # optional, default 22
       'secret': 'admin',      # this is the enable password
       'verbose': True         # optional, default False
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)

# sending a command and getting the output
output = connection.send_command('sh ip int brief')
print(output)

# closing the connection
print('Closing connection')
connection.disconnect()

