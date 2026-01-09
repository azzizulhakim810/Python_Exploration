class BaseChai:
  def __init__(self, type_):
    self.type = type_

  # Method 
  def prepare(self):
    print(f"Preparing {self.type} chai....")

# Inheritance
class GingerChai(BaseChai): # Inherite from parent
  
  # Method 
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

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.chai.prepare()
fancy.chai.add_spices()