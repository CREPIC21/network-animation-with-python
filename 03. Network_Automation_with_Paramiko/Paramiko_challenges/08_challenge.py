"""
A Network Engineer has created this Python(network_engineer_03.py) script that executes show ip interface brief on a
remote Cisco Router and displays the output.
However, since there is a single error in the script it can't display the output of the command.
Your task is to troubleshoot the issue and solve it so that it works as expected.
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
shell.send('terminal length 0\n')
# to see the command output we need in the end of command place "\n" as these is the enter key hit when executing commands on devices
shell.send('show ip int brief\n')
time.sleep(1)

output = shell.recv(100000)
# decoding from bytes to string
output = output.decode()
print(output)


if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()