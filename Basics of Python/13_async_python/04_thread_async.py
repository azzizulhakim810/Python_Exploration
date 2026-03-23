import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def check_stock(item):
  print(f"Checking {item} in store...")
  time.sleep(3) # Blocking Operation
  return f"{item} stock: 42"

async def main():
  loop = asyncio.get_running_loop() #similar to event loop
  with ThreadPoolExecutor() as pool:
    result = await loop.run_in_executor(pool, check_stock, "Masala Chai") # It runs the pool, the function & pass args [pool, target, data]
    print(result)

asyncio.run(main())

# Real Life example

# What This Code Does Instead
# The waiter (async event loop) takes your order and says:
# "I'll hand this to the kitchen staff and go serve other tables while they cook."
# The kitchen staff (ThreadPoolExecutor/thread) handles the slow, blocking work — checking stock — in a separate worker thread.
# await loop.run_in_executor(...) is the waiter handing off the task and saying:
# "Call me when it's ready."

# ----------------------------------------------------

# Why Not Just Use async Directly?
# Because check_stock uses time.sleep(3) — a blocking call that can't be made async (it's old/third-party code). So instead of rewriting it, you run it in a thread where blocking is perfectly fine, and let asyncio stay free to do other things.

# Key idea: run_in_executor is a bridge between the async world and blocking code — best of both worlds.