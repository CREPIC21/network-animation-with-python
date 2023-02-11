"""
Consider the custom Telnet Class developed in the course: telnet_class_improved.py
Add a new method called send_from_file() that receives as an argument a text file with commands and sends all
the commands to the remote device to be executed.
An example of a text file with commands: text_files/commands_02.txt
"""
import time
import telnetlib

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
            print(commands)
            self.send_from_list(commands)

    def show(self):
        output = self.tn.read_all().decode('utf-8')
        return output

command_list = ['enable', 'admin', 'conf t', 'int loopback 5', 'ip address 5.5.5.5 255.255.255.255', 'end', 'terminal length 0', 'show ip interface brief', 'exit']

router_01 = Device(host='192.168.122.4', username='admin', password='admin')
router_01.connect()
router_01.authenticate()
# router_01.send_from_list(command_list)
router_01.send_from_file('./text_files/commands_02.txt')
output = router_01.show()
print(output)
