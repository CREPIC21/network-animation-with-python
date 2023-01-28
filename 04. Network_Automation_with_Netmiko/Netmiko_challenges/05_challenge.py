"""
Change the solution from the previous challenge(04_challenge.py) so that the script saves the output of each command
into its own file.
The name of the file should contain the router’s hostname.
"""

from netmiko import ConnectHandler

with open('./testing_text_files/router_info.txt') as f:
    info = f.readline().split(':')

def write_to_file(file_name, command_output):
    with open(file_name, 'w') as f:
        f.write(command_output)

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