import paramiko
import time
import getpass

# asking for username to connect via SSH
username = input("Username: ")
# creating an ssh client object
ssh_client = paramiko.SSHClient()
print(type(ssh_client))

# this will accept the host key, message that we see when using ssh to connect to the server
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# using getpass to ask the user for the password instead hard coding it in the linux arguments, it works in Pycharm but better to run the script in the terminal
password = getpass.getpass('Enter password: ')

#### replace the username and password with your linux username and password ####
linux = {'hostname': '172.20.231.241', 'port': '22', 'username': username, 'password': password}
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

new_user_name = input("Enter new user name to add: ")
command = f'sudo useradd -m -d /home/{new_user_name} -s /bin/bash {new_user_name}\n'
stdin, stdout, stderr = ssh_client.exec_command(command=command, get_pty=True)

#### replace the password with your linux root password ####
stdin.write(f'{password}\n')
time.sleep(2)

print(f'New user {new_user_name} has been created.')

display_etc_passwd = input('Display the users ? <y|n>: ')
if display_etc_passwd == "y":
    stdin, stdout, stderr = ssh_client.exec_command('cat /etc/passwd\n')
    print(stdout.read().decode())

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()