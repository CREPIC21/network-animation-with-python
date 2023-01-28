"""
Change the solution from the previous challenge(05_challenge.py) so that the script will prompt for both the user
that authenticates and the enable passwords securely (use getpass module).
Run the script in the terminal (you can not run it in PyCharm).
"""

from netmiko import ConnectHandler
import getpass

# asking for host IP to connect to
host_ip = input('Host IP to connect to: ')

# using getpass to ask the user for the password instead hard coding it in the router arguments, it works in Pycharm but better to run the script in the terminal
password = getpass.getpass('Enter password: ')

def write_to_file(file_name, command_output):
    with open(file_name, 'w') as f:
        f.write(command_output)

# creating a dictionary for the device to connect to
cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': host_ip,
       'username': 'admin',
       'password': password,
       'port': 22,             # optional, default 22
       'secret': password,      # this is the enable password
       'verbose': True         # optional, default False
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)

# entering the enabled mode on the device
connection.enable()

# checking in which mode are we
prompt = connection.find_prompt()

# saving router hostname
router_hostname = prompt[:-1]

commands_outputs = []

output_1 = connection.send_command('show ip int brief')
# print(output_1)
write_to_file(f'./testing_text_files/{router_hostname}_int_brief', output_1)
print('#'*80)
output_2 = connection.send_command('show run')
write_to_file(f'./testing_text_files/{router_hostname}_show_run', output_2)
# print(output_2)

# closing the connection
print('Closing connection')
connection.disconnect()