"""
Create a Python script that connects to a Cisco Router using SSH and Netmiko. The script should create an
ACL (access control list) by executing the following 3 commands:
- access-list 101 permit tcp any any eq 80
- access-list 101 permit tcp any any eq 443
- access-list 101 deny ip any any
Note: Try to execute the commands by a single method call.
"""

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

# entering the enabled mode on the device
print('Entering the enable mode...')
connection.enable()

# entering config mode
print('Entering the global configuration mode...')
connection.config_mode()

# sending a command and getting the output
print('Creating access lists...')
cm1 = connection.send_config_set(['access-list 101 permit tcp any any eq 80', 'access-list 101 permit tcp any any eq 443', 'access-list 101 deny ip any any'])
print(cm1)

# closing the connection
print('Closing connection')
connection.disconnect()