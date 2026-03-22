import asyncio
import aiohttp

# Async individual operation to set in a sequence
async def fetch_url(session, url):
  async with session.get(url) as response:
    print(f"Fetched {url} with status {response.status}")


# contains all the async work in a row
async def main():
  urls = ["https://httpbin.org/delay/2"] * 3
  async with aiohttp.ClientSession() as session:
    # tasks = [t1, t2, t3]
    tasks = [fetch_url(session, url) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main())