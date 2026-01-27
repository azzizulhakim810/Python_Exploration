def process_order(item, quantity):
  try:
    price = {"masala": 20}[item]
    cost = price * quantity
    print(f"total cost is {cost}")
  except KeyError:
    print("The specified item is not available in the menu.")
  except TypeError:
    print("Quantity must be a number.")

process_order("masala", "two")  # This will raise a TypeError

process_order("cardamom", 2) # This will raise a KeyError
