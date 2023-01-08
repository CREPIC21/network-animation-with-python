import paramiko

# creating an ssh client object
ssh_client = paramiko.SSHClient()
print(type(ssh_client))

# this will accept the host key, message that we see when using ssh to connect to the server
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('Connecting to 192.168.122.2')
### connecting to the ssh demon that runs on networking device on gns3 ###
# 1. using arguments
# ssh_client.connect(hostname='192.168.122.2', port='22', username='admin', password='admin',
#                    look_for_keys=False, allow_agent=False)

# 2. using **kwargs and arguments unpacking
router = {'hostname': '192.168.122.2', 'port': '22', 'username': 'admin', 'password': 'admin'}
# double ** will unpack the dictionary
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

# checking if the connection is active
print(ssh_client.get_transport().is_active())

# # sending commands
# # ...
#
print('Closing connection')
ssh_client.close()