"""
Create a Python script that connects to a Cisco Router using SSH and Netmiko. The script should create an
ACL (access control list) by executing the following 3 commands:
- access-list 101 permit tcp any any eq 80
- access-list 101 permit tcp any any eq 443
- access-list 101 deny ip any any
Note: Try to execute the commands by a single method call.
"""