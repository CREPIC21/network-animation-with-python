from napalm import get_network_driver

driver = get_network_driver('ios') # cisco ios

optional_args = {'secret': 'admin'} # enable password

# ssh connection using napalm
ios = driver('192.168.122.4', 'admin', 'admin', optional_args=optional_args)
# open the connection
ios.open()

### displaying napalm methods that we can use on the connected device 
print(dir(ios))

# close the connection
ios.close()