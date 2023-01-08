import paramiko
import time
import getpass

# creating an ssh client object
ssh_client = paramiko.SSHClient()
print(type(ssh_client))

# this will accept the host key, message that we see when using ssh to connect to the server
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# print('Connecting to 192.168.122.2')
#### replace the username and password with your linux username and password ####
linux = {'hostname': '172.25.239.185', 'port': '22', 'username': 'username', 'password': 'password'}
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

# this will request interactive shell session on the channel
shell = ssh_client.invoke_shell()

shell.send('cat /etc/passwd\n')
time.sleep(1)

shell.send('sudo cat /etc/shadow\n')
#### replace the password with your linux root password ####
shell.send('root_password\n')
time.sleep(1)

output = shell.recv(10000).decode()
print(output)

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()

"""IMPORTANT"""
"""
- to ssh in linux machine ssh client needs to be installed and enabled on linux machine
-- https://www.cyberciti.biz/faq/ubuntu-linux-install-openssh-server/
"""

