import threading

jersey_stock = 0

def restock():
  global jersey_stock
  for _ in range(10000):
    jersey_stock += 1


threads = [threading.Thread(target=restock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print(f"Chai Stock", jersey_stock)

# Race condition → threads run freely and corrupt data by trampling each other's writes. The program finishes but gives a wrong answer.