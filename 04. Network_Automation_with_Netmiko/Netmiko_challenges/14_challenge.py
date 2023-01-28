"""
Change the solution from the previous challenge(13_challenge.py) so that the function receives a list of global
configuration commands as its second argument and executes those commands on the device using Netmiko.
Example:
cmd = ['no router rip', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'end', 'sh ip int loopback 0']
execute(cisco_device, cmd)
"""