from napalm import get_network_driver

driver = get_network_driver('ios')

ios = driver()