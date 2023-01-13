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
linux = {'hostname': '172.20.231.241', 'port': '22', 'username': 'username', 'password': 'password'}
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('sudo useradd u2\n', get_pty=True)

#### replace the password with your linux root password ####
stdin.write('root_password\n')
time.sleep(2)

stdin, stdout, stderr = ssh_client.exec_command('cat /etc/passwd\n')
print(stdout.read().decode())

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()

"""IMPORTANT"""
"""
- to ssh in linux machine ssh client needs to be installed and enabled on linux machine
-- https://www.cyberciti.biz/faq/ubuntu-linux-install-openssh-server/
"""

