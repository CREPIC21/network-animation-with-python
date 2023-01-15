"""
Consider myparamiko.py script developed in the course.
Add a new function called send_from_file() that receives as an argument a text file with commands and sends all
commands to the remote device to be executed.
An example of a text file with commands in commands.txt
"""
import paramiko
import time

def connect(server_ip, server_port, user, passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {server_ip}')
    ssh_client.connect(hostname=server_ip, port=server_port, username=user, password=passwd,
                       look_for_keys=False, allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timout=1):
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timout)

def send_commands_from_list(shell, commands):
    for command in commands:
        print(command)
        send_command(shell, command)

# SOLUTION
def send_commands_from_text_file(shell, text_file_location):
    with open(text_file_location, 'r') as f:
        commands = f.read().splitlines()
        print(commands)
        send_commands_from_list(shell, commands)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()

if __name__ == '__main__':
    router1 = {'server_ip': '192.168.122.4', 'server_port': '22', 'user':'admin', 'passwd':'admin'}
    client = connect(**router1)
    shell = get_shell(client)

    # send_command(shell, 'enable')
    # send_command(shell, 'admin') # this is the enable password
    # send_command(shell, 'term len 0')
    # send_command(shell, 'sh version')
    # send_command(shell, 'sh ip int brief')

    # commands = ['show ip protocols', 'show ip interface brief', 'show ip interface brief']
    # send_commands_from_list(shell, commands)

    send_commands_from_text_file(shell, 'commands.txt')

    output = show(shell)
    print(output)