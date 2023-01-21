from netmiko import ConnectHandler

with open('devices.txt') as f:
	devices = f.read().splitlines()
	print(devices)
	
device_list = list()


# creating a dictionary for each device to connect to
for ip in devices:
	cisco_device = {
	       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
	       'host': ip,
	       'username': 'admin',
	       'password': 'admin',
	       'port': 22,             # optional, default 22
	       'secret': 'admin',      # this is the enable password
	       'verbose': True         # optional, default False
	       }
	device_list.append(cisco_device)
	
print(device_list)
# exit(1)

for device in device_list:
	# connecting to the device and returning an ssh connection object
	connection = ConnectHandler(**device)

	# entering the enabled mode on the device
	print('Entering enabled mode...')
	connection.enable()
	
	file = input(f'Enter a configuration file(use a valid path) for {device["host"]}: ')
	
	print(f'Running commands from file: {file} on device: {device["host"]}')
	output = connection.send_config_from_file(file)
	print(output)

	# closing the connection
	print('Closing connection')
	connection.disconnect()
	
	print('#' * 20)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
