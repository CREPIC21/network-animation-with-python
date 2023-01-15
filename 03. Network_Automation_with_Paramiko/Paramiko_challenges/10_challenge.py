"""
Create a Python script that connects to a Cisco Router using SSH and Paramiko and executes all the commands
from a text file.
An example of a text file with commands in commands.txt
"""
import paramiko
import time

# creating an ssh client object
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('Connecting to 192.168.122.4')
ssh_client.connect(hostname='192.168.122.4', port='22', username='admin', password='admin',
                   look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()
with open('commands.txt', 'r') as f:
    commands = f.read().splitlines()
    print(commands)

for cmd in commands:
    print(f'Running command: {cmd}...')
    shell.send(f'{cmd}\n')
    time.sleep(1)

output = shell.recv(100000)
# decoding from bytes to string
output = output.decode()
print(output)


if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()