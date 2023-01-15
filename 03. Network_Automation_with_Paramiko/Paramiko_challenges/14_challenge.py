"""
Consider a topology with multiple devices like topology.png.
Create a function called execute_command() that takes 2 arguments: a dictionary with information about the device
(ip, port, credentials) and a show command to execute on the device.
Using a for loop iterate over the routers in the topology and call the function for each router.
"""

import myparamiko

router1 = {'server_ip': '192.168.122.4', 'server_port': '22', 'user': 'admin', 'passwd': 'admin', 'config':'router01_ospf.txt'}
router2 = {'server_ip': '192.168.122.3', 'server_port': '22', 'user': 'admin', 'passwd': 'admin', 'config':'router02_ospf.txt'}
router3 = {'server_ip': '192.168.122.8', 'server_port': '22', 'user': 'admin', 'passwd': 'admin', 'config':'router03_ospf.txt'}

all_routers = [router1, router2, router3]
print(all_routers)

def execute_command(device_info, command):
    client = myparamiko.connect(**device_info)
    shell = myparamiko.get_shell(client)
    myparamiko.send_command(shell, 'enable')
    myparamiko.send_command(shell, 'admin')
    myparamiko.send_command(shell, 'term len 0')
    myparamiko.send_command(shell, command)
    output = myparamiko.show(shell)
    print(output)
    myparamiko.close(client)


for router in all_routers:
    execute_command(router, "show ip interface brief")