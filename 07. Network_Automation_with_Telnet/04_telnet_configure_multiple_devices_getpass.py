"""
The telnetlib (as well as many other libraries) are working with bytes, not strings. This is because bytes are how the information is represented, 
transmitted and stored.
So in the case of telnet you can not use something else, only bytes and you convert them to str.
"""

import telnetlib
import time
import getpass

router_01 = {'host': '192.168.122.4', 'user': 'admin'}
router_02 = {'host': '192.168.122.3', 'user': 'admin'}
router_03 = {'host': '192.168.122.8', 'user': 'admin'}

routers = [router_01, router_02, router_03]

for router in routers:
    print(f'Connecting to {router["host"]}')
    password = getpass.getpass('Enter password: ')
    # creating telnet object
    tn = telnetlib.Telnet(host=router["host"], port='23')

    # pausing the script when telnet is asking for username and password and then we will be logged in
    tn.read_until(b'Username: ')
    tn.write(router["user"].encode() + b'\n')

    tn.read_until(b'Password: ')
    tn.write(password.encode() + b'\n')

    # sending the command in bytes
    tn.write(b'terminal length 0\n')
    tn.write(b'enable\n')
    tn.write(password.encode() + b'\n')
    tn.write(b'conf t\n')
    tn.write(b'ip route 0.0.0.0 0.0.0.0 e0/0 192.168.122.1\n')
    tn.write(b'end\n')
    tn.write(b'show ip route\n')
    tn.write(b'exit\n')
    time.sleep(1)

    # reading all the data from the connection buffer, output is in bytes and we have to decode it to string
    output = tn.read_all()
    print(type(output))
    output = output.decode()
    print(output)
    print('#'*50)

### IMPORTANT - Router Telnet Configuration ###
"""
- username admin secret admin
- line vty 0 4
-- login local
-- transport input telnet ssh

- GNS3 topology used: ospf-paramiko-automation
"""