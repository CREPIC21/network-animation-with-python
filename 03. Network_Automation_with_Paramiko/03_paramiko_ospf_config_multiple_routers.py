import paramiko
import time
import getpass

# creating an ssh client object
ssh_client = paramiko.SSHClient()
print(type(ssh_client))

# this will accept the host key, message that we see when using ssh to connect to the server
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# print('Connecting to 192.168.122.2')

# connecting to the ssh demon that runs on networking device on gns3
router1 = {'hostname': '192.168.122.4', 'port': '22', 'username': 'admin', 'password': 'admin'}
router2 = {'hostname': '192.168.122.3', 'port': '22', 'username': 'admin', 'password': 'admin'}
router3 = {'hostname': '192.168.122.8', 'port': '22', 'username': 'admin', 'password': 'admin'}

routers = [router1, router2, router3]

for router in routers:
    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    # this will request interactive shell session on the channel
    shell = ssh_client.invoke_shell()

    shell.send('enable\n')
    shell.send('admin\n')
    shell.send('conf t\n')
    shell.send('router ospf 1\n')
    shell.send('network 0.0.0.0 0.0.0.0 area 1\n')
    shell.send('end\n')
    shell.send('terminal length 0\n')
    shell.send('show ip protocols\n')
    time.sleep(2)

    # converting bytes to string
    output = shell.recv(10000).decode()
    print(output)

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()