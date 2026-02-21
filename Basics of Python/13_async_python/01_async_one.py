import asyncio

async def brew_chai():
  print(f"Brewing Chai...")
  await asyncio.sleep(2)
  print(f"Chai is ready")

asyncio.run(brew_chai())