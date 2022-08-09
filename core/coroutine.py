import asyncio
import time


async def g():
    # Pause here and come back to g() when counter() is ready
    r = await count()
    return r

# The syntax async def introduces either a native coroutine or an asynchronous generator.
# To call a coroutine function, you must await it to get its results.
#  You can only use await in the body of async def coroutines.
#  an awaitable object is either (1) another coroutine or (2) an object defining an .__await__() dunder method that returns an iterator.


async def count():
    print("One")
# The keyword await passes function control back to the event loop
# It suspends the execution of the surrounding coroutine.)
    await asyncio.sleep(1)
    print("Two")


async def main():
    # await asyncio.gather(count(), count(), count())
    await asyncio.gather(g(), g(), g())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
