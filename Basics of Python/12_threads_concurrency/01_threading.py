# One Core, Multi Threads - Works concurrently

import threading
import time

def take_orders():
  for i in range(1, 4):
    print(f"Taking order for ${i}")
    time.sleep(2)



def brew_chai():
  for i in range(1, 4):
    print(f"Brewing Chai for {i}")
    time.sleep(3)

# It runs sequentially before using thread
# take_orders()
# brew_chai()

# Output
# Taking order for $1
# Taking order for $2
# Taking order for $3
# Brewing Chai for 1
# Brewing Chai for 2
# Brewing Chai for 3


# creating threads 
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

# start the threads
order_thread.start()
brew_thread.start()

# If you now print this below, it prints before the whole process finished 
# print(f"All orders taken & chai brewed")

# Output 
# Taking order for $1
# Brewing Chai for 1
# All orders taken & chai brewed
# Taking order for $2
# Brewing Chai for 2
# Taking order for $3
# Brewing Chai for 3

# So Wait for both to finish 
order_thread.join()
brew_thread.join()

print(f"All orders taken & chai brewed")

# The fianl output 
# Taking order for $1
# Brewing Chai for 1
# Taking order for $2
# Brewing Chai for 2
# Taking order for $3
# Brewing Chai for 3
# All orders taken & chai brewed