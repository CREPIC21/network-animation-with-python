from netmiko import ConnectHandler
import getpass

# asking for username to connect via SSH
username = input("Username: ")
# using getpass to ask the user for the password instead hard coding it in the router arguments, it works in Pycharm but better to run the script in the terminal
# password = getpass.getpass('Enter password: ')
password = input('Enter password: ')
# creating a dictionary for the device to connect to
linux = {
       'device_type': 'linux',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '192.168.227.129',
       'username': username,
       'password': password,
       'port': 22,             # optional, default 22
       'secret': password,       # SUDO password
       'verbose': True         # optional, default False
       }

# connecting to the device and returning an ssh connection object
connection = ConnectHandler(**linux)

# becoming the root
connection.enable()  # equivalent to "sudo su"

# installing apache2
# -y -> it will assume yes as answer to all prompts and run interactively as when scripting there is nobody to answer yes or no
try:
       output = connection.send_command('apt update && apt install -y apache2', read_timeout=90)
       print(output)
finally:
       print("Apache2 installed")

# closing the connection
print('Closing connection')
connection.disconnect()

### IMPORTANT ###
"""
- check to which groups user belongs to --> "id"
- check if apache 2 is installed --> "dpkg --get-selections | grep apache2"
- delete apache2 from Ubuntu --> https://www.programbr.com/ubuntu/permanently-remove-uninstall-apache2-from-ubuntu/
"""