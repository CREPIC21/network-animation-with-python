from netmiko import ConnectHandler
from datetime import datetime
import time
import threading

start = time.time()

def backup(device):
	# connecting to the device and returning an ssh connection object
	connection = ConnectHandler(**device)

	# entering the enabled mode on the device
	print('Entering enabled mode...')
	connection.enable()

	# getting the router configuration
	output = connection.send_command('show run')
	# print(output)
	# getting the router hostname and removing the '#' sing using slicing
	router_hostname = connection.find_prompt()[0:-1]
	# print(router_hostname)
	
	now = datetime.now()
	year = now.year
	month = now.month
	day = now.day
	hour = now.hour
	minute = now.minute

	# creating a name for the backup file
	filename = f'{router_hostname}_{year}--{month}--{day}_backup.txt'

	# saving the configuration to backup file
	with open(filename, 'w') as backup:
		backup.write(output)
		print(f'Backup of {router_hostname} completed successfully.')
		print('#' * 20)

	# closing the connection
	print('Closing connection...')
	connection.disconnect()

with open('devices.txt') as f:
	devices = f.read().splitlines()
	# print(devices)

threads = list()
# creating a dictionary for the each device to connect to
for ip in devices:
	device = {
	       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
	       'host': ip,
	       'username': 'admin',
	       'password': 'admin',
	       'port': 22,             # optional, default 22
	       'secret': 'admin',      # this is the enable password
	       'verbose': True         # optional, default False
	       }
	# backup(device)
	th = threading.Thread(target=backup, args=(device,)) # adding a comma after the device will change the type to tuple
	# appending each thread to the thread list
	threads.append(th)
	
# starting each thread in for loop
for th in threads:
	th.start()
	
# waiting for threads to finish
for th in threads:
	th.join() # join method will make the main program wait for each thread to finish executing


end = time.time()
# getting the total execution time of the script in seconds
print(f'Total execution time: {end-start}')











