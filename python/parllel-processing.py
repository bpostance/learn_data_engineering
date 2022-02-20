import asyncio
import time

## multiple task
async def say_hello(name):
    await asyncio.sleep(3)
    print("Hello-%s" % name)

async def main():
    await say_hello("Ben")
    await say_hello("Jenny")

start_time = time.time()
asyncio.run(main())
print(f"--- {time.time() - start_time:.5f} seconds ---\n\r")