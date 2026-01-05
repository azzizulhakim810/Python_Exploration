# One way to import -------------------------------
# import recipes.flavors

# print(recipes.flavors.elachi_chai())


# Another way to import ---------------------------
from recipes.flavors import ginger_chai, elachi_chai

print(ginger_chai())


# The other way to import --------------------------
from recipes.flavors import ginger_chai as g  # Type alias

print(g())


# It's a way but not recommended -------------------
from .recipes.flavors import ginger_chai
print(ginger_chai())