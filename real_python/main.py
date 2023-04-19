import asyncio
import time
async def count():
    print('One')
    await asyncio.sleep(1)
    print('Two')

async def main():
    await asyncio.gather(count(), count(), count())

def count_sync():
    print('One')
    time.sleep(1)
    print('Two')

def main_sync():
    count_sync()
    count_sync()
    count_sync()


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Program executed in {elapsed:0.2f} seconds")

    s = time.perf_counter()
    main_sync()
    elapsed = time.perf_counter() - s
    print(f"Program executed in {elapsed:0.2f} seconds")