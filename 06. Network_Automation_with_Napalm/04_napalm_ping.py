from napalm import get_network_driver
import json

driver = get_network_driver('ios') # cisco ios

optional_args = {'secret': 'admin'} # enable password

# ssh connection using napalm
ios = driver('192.168.122.4', 'admin', 'admin', optional_args=optional_args)
# open the connection
ios.open()

# start your code
# output = ios.ping(destination='192.168.122.8) 
output = ios.ping(destination='192.168.122.8', source='1.1.1.1', count=2) # extended ping from loopback interface
ping = json.dumps(output, sort_keys=True, indent=4)
print(ping)

# end your code and close the connection
ios.close()