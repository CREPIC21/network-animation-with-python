"""
Consider a topology with multiple devices like topology.png.
For each device in the topology, you have a Python dictionary that stores the SSH connection information (IP, port, username, password)
but also a filename that contains the commands to be sent to that device.

Example:
router1 = {'server_ip': '192.168.122.10', 'server_port': '22', 'user':'u1', 'passwd':'cisco', 'config':'ospf.txt'}
router2 = {'server_ip': '192.168.122.20', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco', 'config':'eigrp.txt'}
router3 = {'server_ip': '192.168.122.30', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco', 'config':'router3.conf'}

Create a Python script that connects to each device using SSH and Paramiko and executes the commands from the file
(which is the value of the dictionary config key).

Use myparamiko.py that was developed in the course or create the script from scratch.
"""
import myparamiko

router1 = {'server_ip': '192.168.122.4', 'server_port': '22', 'user': 'admin', 'passwd': 'admin', 'config':'router01_ospf.txt'}
router2 = {'server_ip': '192.168.122.3', 'server_port': '22', 'user': 'admin', 'passwd': 'admin', 'config':'router02_ospf.txt'}
router3 = {'server_ip': '192.168.122.8', 'server_port': '22', 'user': 'admin', 'passwd': 'admin', 'config':'router03_ospf.txt'}

all_routers = [router1, router2, router3]
print(all_routers)

for router in all_routers:
    client = myparamiko.connect(**router)
    shell = myparamiko.get_shell(client)
    myparamiko.send_commands_from_text_file(shell, f'./protocols_config/{router["config"]}')
    output = myparamiko.show(shell)
    print(output)
    myparamiko.close(client)
