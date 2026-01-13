menu = [
  "Masala Chai",
  "Iced Lemon Tea",
  "Green Tea",
  "Iced Peach Tea",
  "Ginger Tea"
]

# List Comprehension =  [expression for item in iterable if condition]
order_tea = [tea for tea in menu if "Iced" in tea] # Using []
measured_tea = [my_tea for my_tea in menu if len(my_tea) < 12]
print("Order: ", order_tea)
print("Measured: ", measured_tea)