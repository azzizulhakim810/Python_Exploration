import threading
import time

def monitor_sublimation_matchine_temp():
  while True:
    print(f"Monitoring tea temperature")
    time.sleep(2)
    
# daemon=False --> Program hangs, never exits 
t = threading.Thread(target=monitor_sublimation_matchine_temp)

t.start()

print(f"The main program done")