"""
Consider a topology with multiple devices like topology.png.
For each device in the topology, you have a Python dictionary that stores the Telnet connection information:
 (IP, username, password) but also a filename that contains the commands to be sent to that device.
Example:
r1 = {'host': '192.168.122.10', 'username': 'u1', 'password': 'cisco', 'config':'ospf.txt'}
r2 = {'host': '192.168.122.20', 'username': 'u1', 'password': 'cisco', 'config':'eigrp.txt'}
r3 = {'host': '192.168.122.30', 'username': 'u1', 'password': 'cisco', 'config':'router3.conf'}
Create a Python script that connects to each device using Telnet and executes the commands from the file 
(which is the value of the dictionary config key).
Use the Telnet Class telnet_class_improved.py that was developed in the course or create the entire Python script from scratch.
"""
import time
import telnetlib

r1 = {'host': '192.168.122.4', 'username': 'admin', 'password': 'admin', 'config':'./ospf_conf/r1_ospf.txt'}
r2 = {'host': '192.168.122.3', 'username': 'admin', 'password': 'admin', 'config':'./ospf_conf/r2_ospf.txt'}
r3 = {'host': '192.168.122.8', 'username': 'admin', 'password': 'admin', 'config':'./ospf_conf/r3_ospf.txt'}

routers = [r1, r2, r3]
# print(routers)

class Device:
    def __init__(self, host, username, password, tn=None):
        self.host = host
        self.username = username
        self.password = password
        self.tn = tn
    
    def connect(self):
        self.tn = telnetlib.Telnet(self.host)
    
    def authenticate(self):
        self.tn.read_until(b'Username: ')
        self.tn.write(self.username.encode() + b'\n')
        self.tn.read_until(b'Password: ')
        self.tn.write(self.password.encode() + b'\n')

    def send(self, command, timeout=0.5):
        print(f'Sending command {command}')
        self.tn.write(command.encode() + b'\n')
        time.sleep(timeout)

    def send_from_list(self, commands):
        for cmd in commands:
            self.send(cmd)

    ### SOLUTION ###
    def send_from_file(self, file_path):
        with open(file_path, 'r') as f:
            commands = f.read().splitlines()
            # print(commands)
            self.send_from_list(commands)

    def show(self):
        output = self.tn.read_all().decode('utf-8')
        return output


for each_router in routers: 
    router = Device(host=each_router['host'], username=each_router['username'], password=each_router['password'])
    router.connect()
    router.authenticate()
    # router_01.send_from_list(command_list)
    router.send_from_file(each_router['config'])
    output = router.show()
    print(output)
    print(f'Router {each_router["host"]} configured.')
    print('#'*50)