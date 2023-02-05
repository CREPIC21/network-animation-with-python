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

    def show(self):
        output = self.tn.read_all().decode('utf-8')
        return output

command_list = ['enable', 'admin', 'conf t', 'int loopback 5', 'ip address 5.5.5.5 255.255.255.255', 'end', 'terminal length 0', 'show ip interface brief', 'exit']

router_01 = Device(host='192.168.122.4', username='admin', password='admin')
router_01.connect()
router_01.authenticate()
# router_01.send('enable')
# router_01.send('admin')
# router_01.send('conf t')
# router_01.send('interface loopback 2')
# router_01.send('ip address 2.2.2.2 255.255.255.255')
# router_01.send('end')
# router_01.send('terminal length 0')
# router_01.send('show ip interface brief')
# router_01.send('exit')
router_01.send_from_list(command_list)
output = router_01.show()
print(output)
