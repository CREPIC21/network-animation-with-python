"""
A Network Engineer has created Python script (scripts/02_script.py) that executes show ip interface brief on a remote
Cisco Router using Telnet and displays the output.
However, instead of the normal output of the command (a string), it displays some sort of gibberish.
Your task is to troubleshoot the issue and solve it so that it displays the entire output correctly.
"""
import telnetlib
import time

# connecting to the remote device (telnet server)
tn = telnetlib.Telnet('192.168.122.4')

tn.read_until(b'Username: ')
tn.write(b'admin\n')  # sending the username

tn.read_until(b'Password: ')
tn.write(b'admin\n')  # sending the user's password


tn.write('terminal length 0\n'.encode())
tn.write(b'show ip int brief\n')
tn.write(b'exit\n')
time.sleep(1)

# getting and printing the output
### SOULTION - we need to decode bytes to the string to represent the data human readable, adding method decode() to the end solves the issue
output = tn.read_all().decode()
print(output)