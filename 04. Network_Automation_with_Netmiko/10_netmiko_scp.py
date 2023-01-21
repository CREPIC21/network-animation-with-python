from netmiko import ConnectHandler
from netmiko import file_transfer

# asking for username to connect via SSH
username = input("Username: ")
# asking for password to connect via SSH
password = input('Enter password: ')
# creating a dictionary for the device to connect to
cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '192.168.122.10',
       'username': username,
       'password': password,
       'port': 22,             # optional, default 22
       'secret': password,       # enable password
       'verbose': True         # optional, default False
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)

transfer_output = file_transfer(connection, source_file='ospf.txt', dest_file='ospf1.txt', file_system='disk0:', direction='put', overwrite_file=True)
print(transfer_output)

# closing the connection
print('Closing connection')
connection.disconnect()

"""
- once the transfer is done got the the router and execute "dir disk0:" and you will see the file there
"""

### IMPORTANT ###
"""
- GNS3 topology used: netmiko_scp
"""

