# using our custom myparamiko module
import myparamiko_module

client = myparamiko_module.connect('192.168.122.4', '22', 'admin', 'admin')
shell = myparamiko_module.get_shell(client)
myparamiko_module.send_command(shell, 'ifconfig')
# myparamiko_module.send_command(shell, 'admin')
# myparamiko_module.send_command(shell, 'terminal length 0')
# myparamiko_module.send_command(shell, 'show version')
# myparamiko_module.send_command(shell, 'show ip interface brief')
output = myparamiko_module.show(shell)
print(output)

