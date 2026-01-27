class BaseChai:
  # create a constructor __init__
  def __init__(self, type_):
    self.type = type_ # constructor variable don't need to be created before initialize, It's the same if you do. It's like type = None before above initialization.

  # Method 
  def prepare(self):
    print(f"Preparing {self.type} chai....")

# Inheritance
class GingerChai(BaseChai): # Inherite from parent
  
  # It's own Method, not present in BaseChai 
  def add_spices(self):
    print(f"Adding Cardamom, Ginger, Cloves")


# Composition
class ChaiShop:
   chai_cls = BaseChai # an attribute which holds a reference of BaseChai

   def __init__(self):
     self.chai = self.chai_cls("Regular") # self.chai holds self.chai_cls reference & pass "Regular" as BaseChai type
    
   def serve(self):
    print(f"Serving {self.chai.type} chai in the shop")
    self.chai.prepare()

class FancyChaiShop(ChaiShop):
  chai_cls = GingerChai # an attribute which holds a reference of GingerChai


# creating object 
shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.chai.prepare()
fancy.chai.add_spices()

# Key Concepts - Super Simple:
# Inheritance (like GingerChai from BaseChai):

# The child gets EVERYTHING the parent has, plus can add its own stuff
# Like you inherit your mom's eye color, but you also have your own personality!

# Composition (like ChaiShop has BaseChai):

# One class USES another class inside it
# Like a shop USES a recipe book, but the shop isn't a recipe book itself
# The shop can say "Hey, make me a chai using this recipe!"


# Does this make sense? Think of inheritance as "is-a" relationship (GingerChai is a BaseChai) and composition as "has-a" relationship (ChaiShop has a chai)! ☕