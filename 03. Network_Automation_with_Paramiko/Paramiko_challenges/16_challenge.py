"""
Change the solution from Challenge #13 to use multithreading and automate the configuration of the routers concurrently.
"""

import myparamiko
from datetime import datetime
import threading

router1 = {'server_ip': '192.168.122.4', 'server_port': '22', 'user': 'admin', 'passwd': 'admin', 'config':'router01_ospf.txt'}
router2 = {'server_ip': '192.168.122.3', 'server_port': '22', 'user': 'admin', 'passwd': 'admin', 'config':'router02_ospf.txt'}
router3 = {'server_ip': '192.168.122.8', 'server_port': '22', 'user': 'admin', 'passwd': 'admin', 'config':'router03_ospf.txt'}

all_routers = [router1, router2, router3]
print(all_routers)

def execute_commands_from_text_file(device_info):
    client = myparamiko.connect(**device_info)
    print(device_info)
    shell = myparamiko.get_shell(client)
    myparamiko.send_commands_from_text_file(shell, f'./protocols_config/{device_info["config"]}')
    output = myparamiko.show(shell)
    print(output)
    myparamiko.close(client)

threads = list()
for router in all_routers:
    # threading will allow the script to run for all three routers in the same time
    th = threading.Thread(target=execute_commands_from_text_file, args=(router, )) # (router, ) -> this will create a tuple
    # appending each thread to the threads list
    threads.append(th)

# starting each thread from the list of threads
for th in threads:
    th.start()

# waiting for all threads to finish, join method will make the main program to wait for each thread to finish executing
for th in threads:
    th.join()