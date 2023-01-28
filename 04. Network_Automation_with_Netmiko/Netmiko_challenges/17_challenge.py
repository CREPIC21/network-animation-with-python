"""
Change the solution of the previous challenge(16_challenge.py) so that the script will work concurrently
(implement multithreading).
"""

from netmiko import ConnectHandler
import threading

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

threads = list()
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
        # execute(cisco_device, 'show arp')
        th = threading.Thread(target=execute, args=(cisco_device, 'show arp',)) # adding a comma after the device will change the type to tuple
        # appending each thread to the thread list
        threads.append(th)
    if ip == '192.168.122.3':
        # execute(cisco_device, 'show ip interface brief')
        th = threading.Thread(target=execute, args=(cisco_device, 'show ip interface brief',)) # adding a comma after the device will change the type to tuple
        # appending each thread to the thread list
        threads.append(th)
    if ip == '192.168.122.8':
        # execute(cisco_device, 'show version')
        th = threading.Thread(target=execute, args=(cisco_device, 'show version',)) # adding a comma after the device will change the type to tuple
        # appending each thread to the thread list
        threads.append(th)
	
# starting each thread in for loop
for th in threads:
	th.start()
	
# waiting for threads to finish
for th in threads:
	th.join() # join method will make the main program wait for each thread to finish executing