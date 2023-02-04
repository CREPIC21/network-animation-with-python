from napalm import get_network_driver
import json

driver = get_network_driver('ios') # cisco ios

optional_args = {'secret': 'admin'} # enable password

# ssh connection using napalm
ios = driver('192.168.122.10', 'admin', 'admin', optional_args=optional_args)
# open the connection
ios.open()

# start your code

# this method will check if there is any difference between configuration in this file and configuration on the router in running config and if there is any difference it will modify router accordingly
## in config.txt there is rip configured while on the router is not
ios.load_replace_candidate(filename='config.txt')

# this method will compare configurations and return/display the output
diff = ios.compare_config()
# print(diff)
if len(diff):
    print(diff)
    print('Commit changes....')
    # commiting the changes if there is a difference between configuration in the file and actual running configuration on the router
    ### this will apply configuration from the config.txt file as well create rollback_config.txt on the router in disk:0, run "dir disk0:" on the router and you will see both configuration files
    # -- to rollback we have to run ios.rollback()
    ios.commit_config()
    print('Done.')
else:
    print('No changes required.')
    ios.discard_config()

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