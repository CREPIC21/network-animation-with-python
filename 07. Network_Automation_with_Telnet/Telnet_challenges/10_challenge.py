"""
Consider a topology with multiple devices like topology.png.
For each device in the topology, you have a Python dictionary that stores the Telnet connection information:
 (IP, username, password) but also a filename that contains the commands to be sent to that device.
Example:
r1 = {'host': '192.168.122.10', 'username': 'u1', 'password': 'cisco', 'config':'ospf.txt'}
r2 = {'host': '192.168.122.20', 'username': 'u1', 'password': 'cisco', 'config':'eigrp.txt'}
r3 = {'host': '192.168.122.30', 'username': 'u1', 'password': 'cisco', 'config':'router3.conf'}
"""