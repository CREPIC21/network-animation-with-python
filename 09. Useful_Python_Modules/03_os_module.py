import os # https://docs.python.org/3/library/os.html

# executes a command
output = os.popen('arp -a').read()
print(output)

# creates new file
os.system('type nul > test.txt')