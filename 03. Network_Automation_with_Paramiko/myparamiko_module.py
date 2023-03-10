import paramiko
import time

def connect(server_ip, server_port, user, passwd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {server_ip}')
    ssh_client.connect(hostname=server_ip, port=server_port, username=user, password=passwd, look_for_keys=False, allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timeout=1):
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timeout)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()

"""
- this code will be executed only when directly running this script
- when we are importing this script to another script as a module then we want to run all the functions with new arguments
"""
if __name__ == '__main__':
    client = connect('192.168.122.4', '22', 'admin', 'admin')
    shell = get_shell(client)
    send_command(shell, 'enable')
    send_command(shell, 'admin')
    send_command(shell, 'terminal length 0')
    send_command(shell, 'show version')
    send_command(shell, 'show ip interface brief')
    output = show(shell)
    print(output)
    close(client)
