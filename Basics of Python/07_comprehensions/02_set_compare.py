# Simple set comprehension ----------------------------------

favorite_chais = [
  "Masala Chai",
  "Green Tea",
  "Masala Chai",
  "Lemon Tea",
  "Green Tea",
  "Elaichi Chai"
]

unique_chai = {chai for chai in favorite_chais}  # Using {}
# print (unique_chai)


# Complex Example (Extract spices from dictionary using set comprehension ------------------

recipes = {
  "Masala Chai": ["ginger", "cardamom", "clove"],
  "Elaichi Chai": [ "cardamom", "milk"],
  "Spicy Chai": ["ginger", "black pepper", "clove"]
}

# Set Comprehension =  {expression for item in iterable if condition (we can use other things like loops instead of condition)} 

# recipes.key() = all keys
# recipes.values() = all values
# recipes.item() = whole item

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients} # we should use the ultimate value(spice) in the first place not "ingredients"

print(unique_spices)