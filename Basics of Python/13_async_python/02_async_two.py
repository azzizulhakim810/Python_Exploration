import asyncio
import time

# asyncronous work
async def brew(name):
  print(f"Brewing {name}...")
  # work asyncronously & take less time 
  await asyncio.sleep(3)

  # work syncronously & take more time 
  # time.sleep(3)

  print(f"{name} is ready")

# contains all the async work in a row
async def main():
  await asyncio.gather(
    brew("Masala Chai"),
    brew("Green Tea"),
    brew("Ginger Chai")
  )

asyncio.run(main())