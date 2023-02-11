"""
Create a Python script that connects to a Cisco Router using Telnet and executes a list of commands.
The commands are saved in a Python list.
An example of a list with commands to execute:
# the second element (cisco) is the enable command
commands = ['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end', 'terminal length 0', 'sh run | i user']
"""
import telnetlib
import time
import getpass

host = '192.168.122.4'
user = 'admin'

commands = ['enable', 'admin', 'conf t', 'username klaker secret admin', 'access-list 1 permit any', 'end', 'terminal length 0', 'sh run | i user']

# connecting to the remote device (telnet server)
tn = telnetlib.Telnet(host)

tn.read_until(b'Username: ')
tn.write(b'admin\n')  # sending the username

# asking user for password
password = getpass.getpass('Enter password: ')

tn.read_until(b'Password: ')
tn.write(password.encode() + b'\n')  # sending the user's password

for cmd in commands:
    tn.write(cmd.encode() + b'\n')
    time.sleep(1)

tn.write(b'exit\n')
time.sleep(1)

# getting and printing the output
output = tn.read_all().decode()
print(output)