"""
Change the solution from Challenge #1 so that it will prompt the user for the SSH password securely (use getpass module).
Run the script in the terminal (you can not run it in PyCharm).
"""
import paramiko
import time
import getpass

# creating an ssh client object
ssh_client = paramiko.SSHClient()
# this will accept the host key, message that we see when using ssh to connect to the server
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# using getpass to ask the user for the password instead hard coding it in the router arguments, it works in Pycharm but better to run the script in the terminal
password = getpass.getpass('Enter password: ')

# connecting to the ssh demon that runs on networking device on gns3
router = {'hostname': '192.168.122.4', 'port': '22', 'username': 'admin', 'password': password}
print(f'Connecting to {router["hostname"]}...')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

# this will request interactive shell session on the channel
shell = ssh_client.invoke_shell()
# this command will ensure that we receive the whole output
shell.send('terminal length 0\n')
# executing show users command
shell.send('show users\n')
time.sleep(1)
# see the output of the command
output = shell.recv(10000)
# output is byte object, we have to convert it to string
output = output.decode('utf-8')
print(output)

# checking if the connection is active
print(ssh_client.get_transport().is_active())

if ssh_client.get_transport().is_active() == True:
    print('Closing connection...')
    ssh_client.close()
    print('Connection closed.')