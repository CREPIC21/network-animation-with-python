import asyncio
import time


# SYNCHRONOUS
def sync_f():
    print('one ', end='')
    time.sleep(1)
    print('two ', end='')


# ASYNCHRONOUS
async def async_f():
    print('one ', end='')
    await asyncio.sleep(1)
    print('two ', end='')


async def main():
    #### Note that there are 3 awaitable objects: coroutines, tasks and futures.

    # tasks = [async_f(), async_f(), async_f()] # same as below
    tasks = [async_f() for _ in range(3)]

    # we schedule the coroutines to run asap by gathering the tasks like this:
    await asyncio.gather(*tasks)


start_async = time.time()
# The entrance point of any asyncio program is asyncio.run(main()), where main() is a top-level coroutine.
# asyncio.run() was introduced in Python 3.7, and calling it creates an event loop and runs a coroutine on it for you. run() creates the event loop.
asyncio.run(main())
end_async = time.time()
print(f'Execution time of asynchronous code: {end_async - start_async}')

print('\n')
start_sync = time.time()
for _ in range(3):
    sync_f()
end_sync = time.time()
print(f'Execution time of synchronous code: {end_sync - start_sync}')

# async def f():
#     pass
#
# async def g():
#     await f() # pause here and come back to g() when f() is ready
