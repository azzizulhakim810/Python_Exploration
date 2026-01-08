class Chai:
  origin = "Bangladesh" # Declearing this called as properties

print(Chai.origin)

Chai.is_hot = True # Assign another property from outside | is_hot is a variable but when we use this inside a class/object, it's called attribute
print("Chai Hot Status: ", Chai.is_hot)


# Creating objects from class Chai --------------------------------

masala = Chai() 
print("Masala Original Country: ", masala.origin)
print("Masala Chai Hot Status: ", masala.is_hot)

masala.is_hot = False
print("Masala Chai Hot Status: ", masala.is_hot)
print("Chai Hot Status: ", Chai.is_hot)

# Putting another property into the object doesn't mean, it'll be available for original class itself 
masala.flavor = "Spicy"
print(f"Masala Flavor: {masala.flavor}")
print(f"Chai Flavor: {Chai.flavor}") # doesn't exist
