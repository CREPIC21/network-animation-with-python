import subprocess # https://docs.python.org/3/library/subprocess.html

cmd_01 = ['arp', '-a']
cmd_02 = ['ping', '-n', '2', '8.8.8.8']

output_01 = subprocess.check_output(cmd_01).decode() # the returned data is represented in bytes, we need to decode it to string
print(output_01)

output_02 = subprocess.check_output(cmd_02).decode() # the returned data is represented in bytes, we need to decode it to string
print(output_02)