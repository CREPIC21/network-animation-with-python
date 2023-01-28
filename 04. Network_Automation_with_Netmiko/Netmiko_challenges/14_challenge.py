"""
Change the solution from the previous challenge(13_challenge.py) so that the function receives a list of global
configuration commands as its second argument and executes those commands on the device using Netmiko.
Example:
cmd = ['no router rip', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'end', 'sh ip int loopback 0']
execute(cisco_device, cmd)
"""

from netmiko import ConnectHandler

def execute(device, commands):
    # connecting to the device and returning an ssh connection object
    connection = ConnectHandler(**device)

    # entering the enabled mode on the device
    print('Entering the enable mode...')
    connection.enable()

    # sending a command and getting the output
    output = connection.send_config_set(commands)
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

cmd = ['no router rip', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'end', 'sh ip int loopback 0']
print('Executing command on cisco router...')
execute(cisco_device, cmd)
