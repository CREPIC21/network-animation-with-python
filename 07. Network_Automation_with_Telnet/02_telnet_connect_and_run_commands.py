"""
The telnetlib (as well as many other libraries) are working with bytes, not strings. This is because bytes are how the information is represented, 
transmitted and stored.
So in the case of telnet you can not use something else, only bytes and you convert them to str.
"""

import telnetlib
import time

host = '192.168.122.10'
port = '23'
user = 'admin'
password = 'admin'

# creating telnet object
tn = telnetlib.Telnet(host=host, port=port)

# pausing the script when telnet is asking for username and password and then we will be logged in
tn.read_until(b'Username: ')
tn.write(user.encode() + b'\n')

tn.read_until(b'Password: ')
tn.write(password.encode() + b'\n')

# sending the command in bytes
tn.write(b'terminal length 0\n')
tn.write(b'show ip interface brief\n')
tn.write('show version\n'.encode())
tn.write(b'enable\n')
tn.write(b'admin\n') # enable password
tn.write(b'show running-config\n')
tn.write(b'exit\n')
time.sleep(1)

# reading all the data from the connection buffer, output is in bytes and we have to decode it to string
output = tn.read_all()
print(type(output))
output = output.decode()
print(output)


### IMPORTANT - Router Telnet Configuration ###
"""
- username admin secret admin
- line vty 0 4
-- login local
-- transport input telnet ssh

- GNS3 topology used: netmiko_scp
"""