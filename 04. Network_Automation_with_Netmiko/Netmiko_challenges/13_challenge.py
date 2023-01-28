"""
Create a function called execute() that has 2 arguments:
- a device of type dictionary
- a command to execute on that device.
After executing the command the function will disconnect.
The function will use Netmiko to connect and execute the command on the device.
Call the function to execute a command on Cisco router and on a Linux Server.
"""

from netmiko import ConnectHandler

def execute(device, command):
    # connecting to the device and returning an ssh connection object
    connection = ConnectHandler(**device)

    # sending a command and getting the output
    output = connection.send_command(command)
    print(output)

    # closing the connection
    print('Closing connection')
    connection.disconnect()

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

# creating a dictionary for the device to connect to
# IMPORTANT -> for linux replace username, password and secret with your own
linux_device = {
       'device_type': 'linux',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '192.168.227.129',
       'username': '',
       'password': '',
       'port': 22,             # optional, default 22
       'secret': '',      # this is the root password
       'verbose': True         # optional, default False
       }

print('Executing command on cisco router...')
execute(cisco_device, 'show arp')
print('#'*50)
print('Executing command on linux...')
execute(linux_device, 'arp')