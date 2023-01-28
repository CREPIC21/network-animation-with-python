"""
Change the solution from the previous challenge(08_challenge.py) so that the script will also display the
commands that were executed.
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

commands = ['access-list 101 permit tcp any any eq 80', 'access-list 101 permit tcp any any eq 443', 'access-list 101 deny ip any any']

# sending a command and getting the output
print('Creating access lists...')
output = connection.send_config_set(commands)
print(output)

# closing the connection
print('Closing connection')
connection.disconnect()