"""
Create a Python script that connects to a Cisco Router using Telnet and executes the show users command in order to
display the logged-in users.
Print out the output of the command.
"""
import telnetlib
import time

host = '192.168.122.4'
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
tn.write(b'show users\n')
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
"""