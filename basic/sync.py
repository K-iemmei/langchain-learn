import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    await say_hello()  # ❌ không await

    print("Done main!")

asyncio.run(main())