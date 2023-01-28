"""
Consider a topology with multiple devices such as topology.png.
Call the function defined at 13_challenge.py for each device in the topology to execute some commands on each device.
The commands that will be executed on each device can be different.
The script should work sequentially.
"""

from netmiko import ConnectHandler

def execute(device, command):
    # connecting to the device and returning an ssh connection object
    connection = ConnectHandler(**device)

    # entering the enabled mode on the device
    print('Entering the enable mode...')
    connection.enable()

    # sending a command and getting the output
    output = connection.send_command(command)
    print(output)

    # closing the connection
    print('Closing connection')
    connection.disconnect()

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
    print(f'Executing command on cisco router {ip}...')
    if ip == '192.168.122.4':
        execute(cisco_device, 'show arp')
    if ip == '192.168.122.3':
        execute(cisco_device, 'show ip interface brief')
    if ip == '192.168.122.8':
        execute(cisco_device, 'show version')