import asyncio


class APIError(Exception):
    pass


async def call_api(message, result, delay, raise_exception=False):
    print(message)
    await asyncio.sleep(delay)

    if raise_exception:
        raise APIError
    else:
        return result


async def main():
    task_1 = asyncio.create_task(
        call_api("Calling API 1...", 1, 1)
    )
    task_2 = asyncio.create_task(
        call_api("Calling API 2...", 2, 2)
    )
    task_3 = asyncio.create_task(
        call_api("Calling API 3...", 3, 3)
    )

    pending = (task_1, task_2, task_3)

    while pending:
        done, pending = await asyncio.wait(pending, timeout=2, return_when=asyncio.FIRST_COMPLETED)
        result = done.pop().result()
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
