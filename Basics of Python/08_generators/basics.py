# Generators - speacial keyword "yield"

# You save memory
# You don't want the results immediately
# Lazy evaluation 

def serve_chai():
  yield "Cup 1: Masala Chai"
  yield "Cup 2: Ginger Chai"
  yield "Cup 3: Elaichi Chai"

stall = serve_chai() # yield pauses the function to call, it's just keep the reference here
for cup in stall: # it's the main calling & printing
  print(cup)


# Another way to show -----------------------------------------------

def get_chai_list():
  return ["Cup 1", "Cup 2", "Cup 3"]

def get_chai_gen():
  yield "Cup 1"
  yield "Cup 2"
  yield "Cup 3"

chai = get_chai_gen() # next pauses the stream & take a break & execute
print(next(chai)) # It's just printing the first one by using next
print(next(chai)) # It's just printing the second one by using next 
print(next(chai)) # It's just printing the third one by using next
# print(next(chai)) # It's showing error