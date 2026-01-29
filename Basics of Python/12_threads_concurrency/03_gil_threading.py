# Global Interpreter Lock (GIL) - provide mutex(mutual exclusive lock)
# We're learning C Python - Classic Python 
# When two or more thread are going to change the same value, this is called race condition

# When a thread is going to enter memory & want to change a value, mutex is enabled by GIL 

import threading
import time

def brew_chai():
  print(f"{threading.current_thread().name} started brewing...")
  count = 0
  for _ in range(100_000_000):
    count += 1
    # print(f"{threading.current_thread().name} - This is count: {count}")
  print(f"{threading.current_thread().name} finished brewing...")
  
# These two threads both are trying to manipulate the count value at the same time, but one enter first & protected by mutex, then left & other enter & do that same 
thread1 = threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"total time taken: {end - start} seconds")