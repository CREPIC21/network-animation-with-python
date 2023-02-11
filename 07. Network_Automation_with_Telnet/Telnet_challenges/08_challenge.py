"""
Create a Python script that connects to a Cisco Router using Telnet and executes all the commands from a text file.
An example of a text file with commands: text_files/commands_01.txt
"""
import telnetlib
import time
import getpass

host = '192.168.122.4'
user = 'admin'

# creating an array of commands from the commands in the text file
with open('./text_files/commands_01.txt', 'r') as f:
    commands = f.read().splitlines()
print(commands)


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