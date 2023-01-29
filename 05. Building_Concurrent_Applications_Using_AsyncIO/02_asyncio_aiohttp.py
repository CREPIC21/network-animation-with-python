"""
The program will grab a web page from a specific URL and save the source code of that web page in file.
"""

import asyncio

# aiohttp is not python standard library, and you have to install it
# - https://docs.aiohttp.org/en/stable/
import aiohttp

# to read or write to files asynchronously we have to use a library called aiofiles
# - https://pypi.org/project/aiofiles/
import aiofiles

# defining a coroutine
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url) # On this line I'm calling the session.get() coroutine and as any coroutine, I must await it.
        html = await response.text()
        return html

# defining another coroutine that writes some text to a file
async def write_to_file(file, text):
    async with aiofiles.open(file, 'w', encoding="utf-8") as f:
        await f.write(text)

# following the classical pattern of an async app, and we'll create the top-level coroutine which is main.
async def main(urls):
    # each coroutine will create a task that will be spawned asynchronously. The tasks will be saved into a list.
    tasks = []
    for url in urls:
        # Constructing the file name to which I write the source code for each url
        file = f'{url.split("//")[-1]}.txt'
        html = await fetch(url)
        tasks.append(write_to_file(file, html))
    # Scheduling the coroutines to run asap by gathering the tasks like this:
    await asyncio.gather(*tasks)

urls = ('https://www.w3schools.com', 'https://www.udemy.com', 'https://python.org')

asyncio.run(main(urls))

