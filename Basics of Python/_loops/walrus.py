# value = 13
# remainder = value % 5

# if remainder:
#   print(f"Not Divisible, remainder is {remainder}")

# ------------------------------------------------- 

# value = 13

# if (remainder := value % 5):
  # print(f"Not Divisible, remainder is {remainder}")

# available_sizes = ["small", "medium", "large"]

# if(requested_sizes := input("Enter your chai cup size: ")) in available_sizes:
#   print(f"Serving {requested_sizes} chai")
# else:
#   print(f"{requested_sizes} size is unavailable")


# -------------------------------------------------


flavors = ["masala", "ginger", "lemon", "mint"]

print(f"Available Flavours: {flavors}")

while (flavor := input("Choose your flavor: ")) not in flavors:
  print(f"Sorry! {flavor} is not available")
print(f"You choose {flavor} chai")