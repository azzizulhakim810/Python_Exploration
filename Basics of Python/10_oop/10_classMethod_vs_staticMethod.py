class ChaiOrder:
  # Create Constructor 
  def __init__(self, tea_type, sweetness, size):
    self.tea_type = tea_type
    self.sweetness = sweetness
    self.size = size

  # Class Method 1 - handle data from dictionary
  @classmethod
  def from_dict(cls, order_data):
    return cls (
      order_data["tea_type"],
      order_data["sweetness"],
      order_data["size"]
    )
  
  # Class Method 2 - handle data from string
  @classmethod
  def from_string(cls, order_string):
    tea_type, sweetness, size = order_string.split("-")
    return cls(tea_type, sweetness, size)
  
  # Static Method
  @staticmethod
  def is_valid_size(size):
    return size in ["Small", "Medium", "Large"]
  
print(ChaiOrder.is_valid_size("Medium"))

# As they are special method, so we don't need to create explicit object 
order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "low", "size": "small"})
order2 = ChaiOrder.from_string("Ginger-Low-High")
order3 = ChaiOrder("Clove", "High", "Medium")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)