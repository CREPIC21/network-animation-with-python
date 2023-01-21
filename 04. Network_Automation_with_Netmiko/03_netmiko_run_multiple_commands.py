from netmiko import ConnectHandler

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

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**cisco_device)

# entering the enabled mode on the device
print('Entering enabled mode...')
connection.enable()

# list of commands
commands = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'username netmiko secret admin']
# string of commands
cmd = 'do show ip int brief;do show version'
# multistring commands
cmd_multistring = """ do show run | section username
do show run | section line con 0

"""
print(connection.find_prompt())
# using the method below we are automaticaly entering global configuration and executing commands, once done this method exists from global configuration mode automaticaly
# if we want to see the commands and output just save the execution to variable and print it
output = connection.send_config_set(commands) 		# commands from the list
output = connection.send_config_set(cmd.split(';')) 	# commands from string
output = connection.send_config_set(cmd_multistring.split('\n')) 	# commands from multistring
print(output)

print(connection.find_prompt())

# saving the configuration
connection.send_command('write memory')

# closing the connection
print('Closing connection')
connection.disconnect()


