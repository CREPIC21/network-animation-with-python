from napalm import get_network_driver
import json

driver = get_network_driver('ios') # cisco ios

optional_args = {'secret': 'admin'} # enable password

# ssh connection using napalm
ios = driver('192.168.122.10', 'admin', 'admin', optional_args=optional_args)
# open the connection
ios.open()

# start your code

answer = input('Rollback?<yes|no>')
if answer == 'yes':
    print('Rolling back...')
    # rollback will apply the last configuration after changes were made with new configuration
    ios.rollback()
    print('Done')
else:
    print('No changes required.')

# end your code and close the connection
ios.close()


### IMPORTANT ###
"""
Before running the script on router we have to execute below commands otherwise napalm could throw an error:
- from config mode:
-- archive
-- path disk0:
"""

"""
- once the transfer is done got the the router and execute "dir disk0:" and you will see the file there
"""

"""
- GNS3 topology used: netmiko_scp
"""