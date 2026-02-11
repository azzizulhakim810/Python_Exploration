import multiprocessing
import time

def cpu_heavy():
  print(f"Crunching some numbers...")
  total = 0
  for i in range(10**8):
    total += i
  print(f"✅ Done")

if __name__ == "__main__":
  start = time.time()
  # Comprehension
  process = [multiprocessing.Process(target=cpu_heavy) for _ in range(2)]

  [t.start() for t in process]
  [t.join() for t in process]

  print(f"Time taken: {time.time() - start:.2f} seconds")

# Result = Time taken: 10.94 seconds