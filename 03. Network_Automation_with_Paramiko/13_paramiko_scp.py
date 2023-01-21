import paramiko
from scp import SCPClient # https://pypi.org/project/scp/
import getpass

# asking for username to connect via SSH
username = input("Username: ")

# creating an ssh client object
ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()

# this will accept the host key, message that we see when using ssh to connect to the server
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# using getpass to ask the user for the password instead hard coding it in the linux arguments, it works in Pycharm but better to run the script in the terminal
password = getpass.getpass('Enter password: ')

#### replace the username and password with your linux username and password ####
linux = {'hostname': '172.20.231.241', 'port': '22', 'username': username, 'password': password}
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

scp = SCPClient(ssh_client.get_transport())

# copy a single file
scp.put('test.txt', '/tmp/testlinux.txt')

# copy a directory
scp.put('testdir', recursive=True, remote_path='/tmp')

# copy a file from remote location
scp.get('/etc/passwd', 'passwd')

scp.close()