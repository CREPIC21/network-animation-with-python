"""
Program will connect and authenticate to Linux VM using asyncssh and run commands
"""

import asyncio

# - https://asyncssh.readthedocs.io/en/latest/
import asyncssh

async def connect_and_run(host, username, password, commands):
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        # 1. Run single command
        # result = await connection.run(command)
        # return result

        # 2. Run multiple commands
        results = []
        for cmd in commands:
            result = await connection.run(cmd)
            results.append(result)
        return results

# command = 'ifconfig'
# result = asyncio.run(connect_and_run('fe80::20c:29ff:fee9:626f', 'danijel', '1212', command))
# print(f'STDOUT:\n {result.stdout}')
# print(f'STDERR:\n {result.stderr}')

commands = ('ifconfig', 'who -a', 'uname -a')
results = asyncio.run(connect_and_run('fe80::20c:29ff:fee9:626f', 'danijel', '1212', commands))
for result in results:
    print(f'STDOUT:\n {result.stdout}')
    print(f'STDERR:\n {result.stderr}')
    print('#'*50)