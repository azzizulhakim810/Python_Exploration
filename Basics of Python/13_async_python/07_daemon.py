import threading
import time

def monitor_sublimation_matchine_temp():
  while True:
    print(f"Monitoring tea temperature")
    time.sleep(2)

t = threading.Thread(target=monitor_sublimation_matchine_temp, daemon=True)

t.start()

print(f"The main program done")