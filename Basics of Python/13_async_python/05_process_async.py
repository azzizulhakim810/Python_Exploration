import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
  return f"🔒 {data[::-1]}"

async def main():
  loop = asyncio.get_running_loop()
  with ProcessPoolExecutor() as pool:
    result = await loop.run_in_executor(pool, encrypt, "Credit_Card_2345")
    print(f"{result}")

if __name__ == "__main__":
  asyncio.run(main())

#  What This Code Does
# Think of it like a bank vault clerk handling a sensitive document.

# The Real Life Scenario
# You're a bank manager (async event loop). A customer hands you their credit card number and asks you to encrypt it for secure storage.
# You don't do it yourself — you pass it to a specialized vault clerk (ThreadPoolExecutor) whose only job is handling sensitive encryption work. While the clerk works, you're free to serve other customers.