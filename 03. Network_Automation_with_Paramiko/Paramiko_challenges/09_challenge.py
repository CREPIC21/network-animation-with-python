"""
Create a Python script that connects to a Cisco Router using SSH and Paramiko and executes a list of commands.
The commands are saved in a Python list.
An example of a list with commands to execute:
# the second element (cisco) is the enable command
commands = ['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end', 'terminal length 0', 'sh run | i user']
"""
import paramiko
import time

# creating an ssh client object
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('Connecting to 192.168.122.4')
ssh_client.connect(hostname='192.168.122.4', port='22', username='admin', password='admin',
                   look_for_keys=False, allow_agent=False)

commands = ['terminal length 0', 'enable', 'admin', 'conf t', 'do show ip int brief', 'do sh running-config']

shell = ssh_client.invoke_shell()
for cmd in commands:
    shell.send(f'{cmd}\n')
    time.sleep(1)

output = shell.recv(100000)
# decoding from bytes to string
output = output.decode()
print(output)


if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()