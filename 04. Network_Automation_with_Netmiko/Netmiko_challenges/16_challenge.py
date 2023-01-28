"""
Consider the solution from the previous challenge(15_challenge.py).
Implement exception handling (try...except) so that if a device in the list is down, the script will move on to the
next one and doesn’t stop and fail when trying to access the device that is down.
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
        try:
            execute(cisco_device, 'show arp')
        except:
            print('Interface DOWN!!!')
    if ip == '192.168.122.3':
        try:
            execute(cisco_device, 'show ip interface brief')
        except:
            print('Interface DOWN!!!')
    if ip == '192.168.122.8':
        try:
            execute(cisco_device, 'show version')
        except:
            print('Interface DOWN!!!')