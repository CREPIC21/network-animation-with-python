"""
Consider a topology with multiple devices such as topology.png.
Create a Python script that connects to each Router using Netmiko, execute show ip interface brief and display the output.
The IP addresses of the routers are saved in a Python list.
"""

from netmiko import ConnectHandler

routers_ips = ['192.168.122.4', '192.168.122.3', '192.168.122.8']

for ip in routers_ips: 
    # creating a dictionary for the device to connect to
    cisco_device = {
        'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
        'host': ip,
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

    # sending a command and getting the output
    print('Executing command...')
    output = connection.send_command('show ip interface brief')
    print(output)

    # closing the connection
    print('Closing connection')
    connection.disconnect()