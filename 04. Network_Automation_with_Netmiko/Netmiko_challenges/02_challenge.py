"""
Change the solution from the previous challenge(01_challenge.py) so that the Python script reads the IP address of
the device, the port, the username, and the password from a file.
The file contains the login information on a single line in the format: IP:PORT:USERNAME:PASSWORD:ENABLE_PASSWORD
Example: 10.1.1.10:22:u1:cisco:cisco
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

# sending a command and getting the output
output = connection.send_command('show arp')
print(output)

# closing the connection
print('Closing connection')
connection.disconnect()