"""
Create a Python script that connects to a Cisco Router using SSH and Netmiko. The script should get the prompt,
process it and then print the hostname part.
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

# checking in which mode are we
prompt = connection.find_prompt()
# router_hostname = prompt.split('>')[0]
router_hostname = prompt[:-1]
print("We are in prompt: " + prompt)
print(f'Router hostname is: {router_hostname}')

# closing the connection
print('Closing connection')
connection.disconnect()