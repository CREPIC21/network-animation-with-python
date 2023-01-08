# using our custom myparamiko module
import myparamiko_module

#### replace the username and password with your linux username and password ####
client = myparamiko_module.connect('172.25.239.185', '22', 'username', 'password')
shell = myparamiko_module.get_shell(client)
myparamiko_module.send_command(shell, 'ifconfig')
myparamiko_module.send_command(shell, 'uname -a')

cmd = 'sudo groupadd developers'
myparamiko_module.send_command(shell, cmd)
#### replace the password with your linux root password ####
myparamiko_module.send_command(shell, 'password', 2)
# myparamiko_module.show(shell) # will flash the buffer, meaning we will only see the output on next commands
myparamiko_module.send_command(shell, 'tail -n 1 /etc/group')

output = myparamiko_module.show(shell)
print(output)

