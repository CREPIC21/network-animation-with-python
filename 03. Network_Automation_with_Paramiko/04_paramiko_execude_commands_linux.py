import paramiko
import time
import getpass

# creating an ssh client object
ssh_client = paramiko.SSHClient()
print(type(ssh_client))

# this will accept the host key, message that we see when using ssh to connect to the server
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# print('Connecting to 192.168.122.2')
router = {'hostname': '192.168.122.2', 'port': '22', 'username': 'admin', 'password': 'xxxx'}
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

# this will request interactive shell session on the channel
shell = ssh_client.invoke_shell()

shell.send('enable\n')
shell.send('admin\n')
shell.send('conf t\n')
time.sleep(1)

output = shell.recv(10000).decode()
print(output)

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()

