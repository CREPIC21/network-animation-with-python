"""
A Network Engineer has created Python script (scripts/01_script.py) that executes show ip interface brief on a remote
Cisco Router using Telnet and displays the output.
However, the script it’s hanging (nothing happens when it’s run).
Your task is to troubleshoot the issue and solve it so that it displays the output of the command.
"""
import telnetlib
import time

# connecting to the remote device (telnet server)
tn = telnetlib.Telnet('192.168.122.4')

tn.read_until(b'Username: ')
tn.write(b'admin\n')  # sending the username

tn.read_until(b'Password: ')
tn.write(b'admin\n')  # sending the user's password

### SOLUTION - script was missing the below "terminal length 0" command which will display the whole output in case router truncates the output
tn.write(b'terminal length 0\n')

tn.write(b'show ip int brief\n')
tn.write(b'exit\n')
time.sleep(1)

# getting and printing the output
output = tn.read_all()
output = output.decode()
print(output)