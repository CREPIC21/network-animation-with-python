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

    def show(self):
        output = self.tn.read_all().decode('utf-8')
        return output

router_01 = {'host': '192.168.122.4', 'user': 'admin', 'password': 'admin', 'enable_password': 'admin', 'loopback_ip': '3.3.3.3'}
router_02 = {'host': '192.168.122.3', 'user': 'admin', 'password': 'admin', 'enable_password': 'admin', 'loopback_ip': '3.3.3.3'}
router_03 = {'host': '192.168.122.8', 'user': 'admin', 'password': 'admin', 'enable_password': 'admin', 'loopback_ip': '3.3.3.3'}

routers = [router_01, router_02, router_03]

for r in routers:
    router = Device(host=r['host'], username=r['user'], password=r['password'])
    router.connect()
    router.authenticate()
    router.send('enable')
    router.send(r['enable_password'])
    router.send('conf t')
    router.send('interface loopback 3')
    router.send(f'ip address {r["loopback_ip"]} 255.255.255.255')
    router.send('end')
    router.send('terminal length 0')
    router.send('show ip interface brief')
    router.send('exit')
    output = router.show()
    print(output)
    print('#'*50)
