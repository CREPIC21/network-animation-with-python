"""
Change the solution from Challenge #14 to use multithreading and execute the command concurrently on all routers
in the topology.
"""
import myparamiko
from datetime import datetime
import threading

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

# for router in all_routers:
#     execute_command(router, "show ip interface brief")

threads = list()
for router in all_routers:
    # threading will allow the script to run for all three routers in the same time
    th = threading.Thread(target=execute_command, args=(router, "show ip interface brief", )) # (router, ) -> this will create a tuple
    # appending each thread to the threads list
    threads.append(th)

# starting each thread from the list of threads
for th in threads:
    th.start()

# waiting for all threads to finish, join method will make the main program to wait for each thread to finish executing
for th in threads:
    th.join()