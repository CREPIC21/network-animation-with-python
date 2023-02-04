from napalm import get_network_driver
import json

driver = get_network_driver('ios') # cisco ios

optional_args = {'secret': 'admin'} # enable password

# ssh connection using napalm
ios = driver('192.168.122.4', 'admin', 'admin', optional_args=optional_args)
# open the connection
ios.open()

# start your code
output_01 = ios.get_facts()
dump_output_01 = json.dumps(output_01, sort_keys=True, indent=4)
print(dump_output_01)

print('#'*100)
output_02 = ios.get_arp_table()
dump_output_02 = json.dumps(output_02, sort_keys=True, indent=4)
print(dump_output_02)

print('#'*100)
output_03 = ios.get_interfaces()
dump_output_03 = json.dumps(output_03, sort_keys=True, indent=4)
print(dump_output_03)

print('#'*100)
output_04 = ios.get_interfaces_counters()
dump_output_04 = json.dumps(output_04, sort_keys=True, indent=4)
print(dump_output_04)

print('#'*100)
output_05 = ios.get_interfaces_ip()
dump_output_05 = json.dumps(output_05, sort_keys=True, indent=4)
print(dump_output_05)

print('#'*100)
output_06 = ios.get_users()
dump_output_06 = json.dumps(output_06, sort_keys=True, indent=4)
print(dump_output_06)


# end your code and close the connection
ios.close()