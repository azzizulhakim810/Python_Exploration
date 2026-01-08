class Chai_Order:
  # define a constructor [ __init__ ]
  def __init__(self, type_, size):
    # inside the constructor, we should initialize the properties 
    self.type = type_ # we can create un-existed properties inside the constructor like type, size. This they are empty string or None
    self.size = size

  # method
  def summary(self):
    return f"{self.size}ml of {self.type} chai"
  
# create instances 
order = Chai_Order("Masala", 200)
order2 = Chai_Order("Ginger", 160)

# method calling 
print(order.summary())
print(order2.summary())

