chai = "Ginger Chai"

def prepare_chai(order):
  print("Preparing", order)

prepare_chai(chai)
print(chai)

# ------------------------------------- 

chai = [5, 3, 8] # list is mutable

def edit_chai_amount(cup):
  cup[2] = 0

edit_chai_amount(chai)
print(chai)

# --------------------------------------

def make_chai(tea, milk, sugar):
  print(tea, milk, sugar)

make_chai("Sylhetti", "Yes", "No") # positional (argument)
make_chai(tea="Chatgaiya", sugar="Yes", milk="No") # Keyword argument


# ----------------------------------------- 

def special_chai(*ingredients, **extras):
  print("Ingredients: ", ingredients)
  print("Extras: ", extras)

special_chai("Cinamon", "Cardamom", sweetener="Honey", foam="Yes")


# -----------------------------------------

# def chai_order(order=[]): # if you asssign the default value empty array, then double function call will make it worse. It's better to use none & make it conditional
def chai_order(order=None):
  if order is None:
   order = []
   order.append("Masala")
  print(order)

chai_order()
chai_order()