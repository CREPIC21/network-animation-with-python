"""
A Network Engineer has created this Python script (scripts/03_script.py) that executes show ip interface brief on a remote
Cisco Router using Telnet and displays the output.
However, the output of the command can’t be displayed as there is an error in the script. The script doesn’t run,
rather it hangs.
Your task is to troubleshoot the issue and solve it so that it works as expected.
"""
import telnetlib
import time

# connecting to the remote device (telnet server)
tn = telnetlib.Telnet('192.168.122.4')

tn.read_until(b'Username: ')
tn.write(b'admin\n')  # sending the username

tn.read_until(b'Password: ')
tn.write(b'admin\n')  # sending the user's password


tn.write(b'terminal length 0\n')
tn.write(b'show ip int brief\n')
### SOLUTION - command was missing the new line character at the end "\n", without it the script will hang
tn.write(b'exit\n')
time.sleep(1)

# getting and printing the output
output = tn.read_all().decode()
print(output)