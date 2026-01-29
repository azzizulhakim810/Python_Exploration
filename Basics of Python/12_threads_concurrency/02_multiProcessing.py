from multiprocessing import Process
import time

def brew_chai(name):
  print(f"Start of {name} chai brewing")
  time.sleep(3)
  print(f"End of {name} chai brewing")


# brew_chai("masala")
 
if __name__ == "__main__":
  chai_makers = [
    Process(target=brew_chai, args=(f"Chai Maker #{i+ 1}", )) # This comma is important, it shows no kwargs
    #self._target(*self._args, **self._kwargs)
    for i in range(3)
  ]
  
  # Start all process
  for p in chai_makers:
    p.start()

  # Wait for all to complete
  for p in chai_makers:
    p.join()

  print("All Chai Served")