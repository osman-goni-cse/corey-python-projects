import asyncio
import time
from asyncio import CancelledError
from asyncio.exceptions import TimeoutError


async def call_api(message, result=1000, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def message_task():
    for _ in range(3):
        await asyncio.sleep(1)
        print("API call is in progress")


async def main():

    task = asyncio.create_task(
        call_api("Apple Stock:", 3000, 5)
    )

    MAX_TIMEOUT = 3

    try:
        await asyncio.wait_for(asyncio.shield(task), timeout=MAX_TIMEOUT)
    except TimeoutError:
        print(f"Task can't be completed within {MAX_TIMEOUT} seconds. It will complete soon.")
        await task
        print('Task is completed')



if __name__ == '__main__':
    asyncio.run(main())