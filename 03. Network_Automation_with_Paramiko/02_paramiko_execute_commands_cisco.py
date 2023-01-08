import paramiko
import time
import getpass

# creating an ssh client object
ssh_client = paramiko.SSHClient()
print(type(ssh_client))

# this will accept the host key, message that we see when using ssh to connect to the server
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('Connecting to 192.168.122.2')
# using getpass to ask the user for the password instead hard coding it in the router arguments, it works in Pycharm but better to run the script in the terminal
password = getpass.getpass('Enter password: ')
# connecting to the ssh demon that runs on networking device on gns3
router = {'hostname': '192.168.122.2', 'port': '22', 'username': 'admin', 'password': password}
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

# this will request interactive shell session on the channel
shell = ssh_client.invoke_shell()
# this command will ensure that we receive the whole output
shell.send('terminal length 0\n')
# sending commands to remote device
shell.send('show version\n')
shell.send('show ip interface brief\n')
# going to sleep for 1 second to give enough time to remote device to execute the command
time.sleep(1)
# see the output of the command
output = shell.recv(10000)
print(type(output))
# output is byte object, we have to convert it to string
output = output.decode('utf-8')
print(output)

# checking if the connection is active
print(ssh_client.get_transport().is_active())

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()