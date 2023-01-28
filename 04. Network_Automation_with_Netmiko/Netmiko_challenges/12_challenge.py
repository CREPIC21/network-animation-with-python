"""
Change the solution from the previous challenge(11_challenge.py) so that the script will save the output to a file
instead of printing it out.
Each filename should contain the hostname and current date.
"""

from netmiko import ConnectHandler

routers_ips = ['192.168.122.4', '192.168.122.3', '192.168.122.8']

def write_to_file(file_name, command_output):
    with open(file_name, 'w') as f:
        f.write(command_output)

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

    # checking in which mode are we
    prompt = connection.find_prompt()
    # saving router hostname
    router_hostname = prompt[:-1]

    # sending a command and getting the output
    print('Executing command...')
    output = connection.send_command('show ip interface brief')
    write_to_file(f'./testing_text_files/{router_hostname}_06_challenge', output)
    print(output)

    # closing the connection
    print('Closing connection')
    connection.disconnect()

