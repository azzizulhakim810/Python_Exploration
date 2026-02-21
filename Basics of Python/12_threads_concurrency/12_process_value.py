from multiprocessing import Process, Value

def increment(counter):
  for _ in range(100000):
    with counter.get_lock():
      counter.value += 1

if __name__ == "__main__":
  counter = Value('i', 0)
  processes = [Process(target=increment, args=(counter, )) for _ in range(4)]
  [p.start() for p in processes]
  [p.join() for p in processes]

  print(f"Final Counter: ", counter.value)

# Shared Value with Lock (Shared State)
# Multiple processes update the same shared variable safely using locks.
# Real-world uses:

# Download manager: Track total bytes downloaded across multiple parallel downloads
# Progress tracking: Multiple workers update a shared progress counter
# Resource counting: Track how many resources (connections, files, etc.) are currently in use across processes
# Distributed counters: Like a website visitor counter updated by multiple server processes

# Key point: Good when multiple processes need to update the same piece of data (but use carefully - locks can slow things down).