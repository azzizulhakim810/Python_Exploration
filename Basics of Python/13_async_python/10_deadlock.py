import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def task1():
  with lock_a:
    print("Task 1 acquired lock a")
    with lock_b:
      print("Task 1 acquired lock b")

def task2():
  with lock_b:
    print("Task 2 acquired lock b")
    with lock_a:
      print("Task 2 acquired lock a")

# The Fix — Always Lock in the Same Order
# def task1():
#     with lock_a:      # Lock A first
#         with lock_b:  # Then B
#             ...

# def task2():
#     with lock_a:      # Lock A first (same order!)
#         with lock_b:  # Then B
#             ...
      

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()


# Deadlock → threads politely wait for each other forever. The program never finishes at all. 