"""
Create a Python script that connects to a Cisco Router using SSH and Paramiko and executes a list of commands.
The commands are saved in a Python list.
An example of a list with commands to execute:
# the second element (cisco) is the enable command
commands = ['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end', 'terminal length 0', 'sh run | i user']
"""