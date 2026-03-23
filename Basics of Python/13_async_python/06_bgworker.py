import asyncio
import threading
import time

def background_worker():
  while True:
    time.sleep(1)
    print(f"Logging the system health")

async def fetch_orders():
  await asyncio.sleep(3)
  print(f"Order Fetched")


threading.Thread(target=background_worker, daemon=True).start()

asyncio.run(fetch_orders())

# The Real Life Scenario
# A health inspector (background_worker) walks around the restaurant every minute checking if everything is okay — fridges, hygiene, stock levels. He never stops. He just keeps doing his rounds forever in the background.
# Meanwhile, a waiter (fetch_orders) is doing his actual job — taking and fetching orders from the kitchen.
# Both are working at the same time, independently. The inspector doesn't wait for the waiter, and the waiter doesn't wait for the inspector.



# What is daemon=True? 🔑
# This is the most important concept here.

# A daemon thread is like a security guard hired only while the restaurant is open.

# Daemon Thread - Normal Thread

# When restaurant closes --> Guard leaves automatically - 🚪Guard keeps standing outside forever 😐

# In code --> Thread dies when main program ends - Thread keeps running, program never exits

# Use case --> Background logging, monitoring - Tasks that MUST finish