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

# checking in which mode are we
prompt = connection.find_prompt()
print("We are in prompt: " + prompt)

# checking if we are in enable mode
if '>' in prompt:
	# entering the enabled mode on the device
	connection.enable()
	prompt = connection.find_prompt()
	print("We are in prompt: " + prompt)

# checking if we are in configuration mode
print(connection.check_config_mode())
if not connection.check_config_mode():
	# entering config mode
	connection.config_mode()
	prompt = connection.find_prompt()
	print("We are in prompt: " + prompt)
	
# once in configuration mode we can run command to create new user
connection.send_command('username danijel secret admin')

# exiting config mode
connection.exit_config_mode()
print(connection.check_config_mode())

# closing the connection
print('Closing connection')
connection.disconnect()
