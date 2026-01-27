chai_menu = {"masala": 20, "ginger": 25, "tulsi": 30}



# print(chai_menu["cardamom"])  # This will raise a KeyError

# print(f"Hello")  # This will not be printed because of the error above

try:
  chai_menu["spice"]  # This will raise a KeyError
except KeyError:
  print("The specified key does not exist in the dictionary.")

print(f"Hello after executing the try-except block")  # This will be printed because the error is handled