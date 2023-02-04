from napalm import get_network_driver
import json

driver = get_network_driver('ios') # cisco ios

optional_args = {'secret': 'admin'} # enable password

# ssh connection using napalm
ios = driver('192.168.122.4', 'admin', 'admin', optional_args=optional_args)
# open the connection
ios.open()

# start your code
output = ios.get_arp_table()
print(output)
# One way of displaying the arp table details
for item in output:
    print(item)

# Another way of displaying the arp table details -> using json
dump = json.dumps(output, sort_keys=True, indent=4)
print('#'*50)
print(dump)
with open('arp.txt', 'w') as f:
    f.write(dump)

# end your code and close the connection
ios.close()