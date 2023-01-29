"""
The program will run linux or windows commands asynchronously.
"""

import asyncio

# creating a coroutine that takes as argument the command that will run asynchronously
async def run(cmd):
    #  To run the command I'll use the create_subprocess_shell() function of the asyncio library.
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()

    # Each Linux command returns a status code which is zero if there was no error and different from zero if there was error.
    print(f'{cmd} exited with status code: {proc.returncode}')

    # if the command has generated any output we can access it by using stdout.decode()
    if stdout:
        print(f'STDOUT:\n{stdout.decode("UTF-8")}')
    if stderr:
        print(f'STDERR:\n{stderr.decode()}')

# defining the top level coroutine which is the async application starting point.
# this coroutine will take a list of commands as argument and spawn a task asynchronously for each command.
async def main(commands):
    tasks = []
    for cmd in commands:
        tasks.append(run(cmd))

    # and we schedule the coroutines to run asap by gathering the tasks.
    await asyncio.gather(*tasks)

# running some random Linux or Windows commands asynchronously.
commands_linux = ('ifconfig', 'ls', 'who', 'uname -a') # linux commands
commands_windows = ('ipconfig', 'dir', 'route dir', 'arp -a')
asyncio.run(main(commands_windows))