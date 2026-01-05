# Built-in 
from functools import wraps

def my_decorator(func):
  @wraps(func) # mention the wrapped function
  def wrapper():
    print("Before function runs")
    func() # calll the function got from parameter
    print("After function runs")
  return wrapper

@my_decorator # It means that It's decorating the next function(greet()). The next line is the parametere function & it goes inside wrapper
def greet():
  print("Hello from greet function")

greet()
print(greet.__name__) # it's printing the function name is "wrapper" as it's wrapped by that function

# So we're gonna install a third party built-in module "wraps". So now it prints the actual function name "greet"