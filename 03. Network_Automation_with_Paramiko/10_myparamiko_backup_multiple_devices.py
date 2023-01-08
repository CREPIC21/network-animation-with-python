# using our custom myparamiko module
import myparamiko_module
from datetime import datetime

#### replace the username and password with your linux username and password ####
router1 = {'server_ip': '192.168.122.4', 'server_port': '22', 'user': 'admin', 'passwd': 'admin'}
router2 = {'server_ip': '192.168.122.3', 'server_port': '22', 'user': 'admin', 'passwd': 'admin'}
router3 = {'server_ip': '192.168.122.8', 'server_port': '22', 'user': 'admin', 'passwd': 'admin'}

routers = [router1, router2, router3]

for router in routers:
    client = myparamiko_module.connect(**router)
    shell = myparamiko_module.get_shell(client)

    myparamiko_module.send_command(shell, 'terminal length 0')
    myparamiko_module.send_command(shell, 'enable')
    myparamiko_module.send_command(shell, 'admin') # enable password
    myparamiko_module.send_command(shell, 'show run')

    output = myparamiko_module.show(shell)
    # print(output)
    output_list = output.splitlines()
    print(output_list)
    output_list = output_list[9:-2]
    print(output_list)
    output = '\n'.join(output_list)
    print(output)

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    file_name = f'./backups/{router["server_ip"]}_{year}-{month}-{day}.txt'

    with open(file_name, 'w') as f:
        f.write(output)

    # closing the connection before closing the script
    myparamiko_module.close(client)