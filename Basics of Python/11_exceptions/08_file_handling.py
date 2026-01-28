# Open, Read, Write Files using open & with open as file -----------------------------------------

# file = open("order.txt", "w")
# try:
#   file.write("Masala Chai- 4 cups")
# finally:
  # file.close()

with open("order.txt", "w") as file:
  file.write("ginger tea - 8 cups")

# This "file" creates two dunders behind the scene, like: 
# file__enter__()
# write
# file__close__()