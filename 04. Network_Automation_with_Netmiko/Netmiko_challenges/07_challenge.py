"""
Create a Python script that connects to a Cisco Router using SSH and Netmiko. The script should create a user and
then save the running configuration of the router.
To create a user execute: username admin secret topsecret command in the global configuration mode.
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
print('Creating a new user...')
cm1 = connection.send_command('username test secret test')
print(cm1)

# exiting from config mode
print('Exiting from the global configuration mode...')
connection.exit_config_mode()

print('Saving the configuration...')
cm2 = connection.send_command('write')

# closing the connection
print('Closing connection')
connection.disconnect()