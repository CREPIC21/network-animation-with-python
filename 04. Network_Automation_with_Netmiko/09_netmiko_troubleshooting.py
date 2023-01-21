from netmiko import ConnectHandler
import time
import logging # https://github.com/ktbyers/netmiko/blob/develop/COMMON_ISSUES.md
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

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

# sending a command and getting the output
# output = connection.send_command('sh ip int brief')
# print(output)

connection.write_channel('show version\n')
time.sleep(2)
output = connection.read_channel()
print(output)

# closing the connection
print('Closing connection')
connection.disconnect()

