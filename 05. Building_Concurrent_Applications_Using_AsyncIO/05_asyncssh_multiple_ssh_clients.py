"""
Program will connect and authenticate to multiple Linux VMs using asyncssh and run commands
"""

import asyncio

# - https://asyncssh.readthedocs.io/en/latest/
import asyncssh

async def run_client(host, username, password, command):
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        return await connection.run(command)

async def run_multiple_clients(hosts):
    tasks = []
    for host in hosts:
        task = run_client(host['host'], host['username'], host['password'], host['command'])
        tasks.append(task)

    results = await asyncio.gather(*tasks, return_exceptions=True)

    i = 0
    for result in results:
        i += 1
        if isinstance(result, Exception):
            print(f'Task {i} failed: {str(result)}')
        elif result.exit_status != 0:
            print(f'Task {i} exited with status: {result.exit_status}')
            print(result.stderr, end='')
        else:
            print(f'Task {i} succeeded.')
            print(result.stdout, end='')
        print('#'*50)

hosts = [
    {
        'host': 'fe80::20c:29ff:fee9:626f',
        'username': 'danijel',
        'password': '1212',
        'command': 'ifconfig'
    },
    {
        'host': 'fe80::20c:29ff:fee9:626f',
        'username': 'danijel',
        'password': '1212',
        'command': 'who -a'
    },
    {
        'host': 'fe80::20c:29ff:fee9:626f',
        'username': 'danijel',
        'password': '1212',
        'command': 'uname -a'
    }
]

asyncio.run(run_multiple_clients(hosts))