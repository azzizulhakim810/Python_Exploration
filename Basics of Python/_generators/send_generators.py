# We can send data to yield & print it 

def chai_customer():
  print("Welcome! What chai would you like?")
  order = yield # Waiting for the order through "send"
  while True:
    print(f"Preparing: {order}")
    order = yield # It's again waiting for another value. Without this line, the console will be printing infinitely

stall = chai_customer()
next(stall) # It's just a call so it'll only print the welcome message

stall.send("Masala Chai") # Now it's printing the order value
stall.send("Elaichi Chai")

