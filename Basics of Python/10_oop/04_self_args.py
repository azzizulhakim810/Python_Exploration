class Chaicup:
  size = 150

  # Creating method - function inside class is called method 
  def describe(self):
    return f"A {self.size}ml chai cup"
  
cup = Chaicup() # Creating the object/instances
print("Cup 1: ", cup.describe()) # Direct calling to method 
print("Direct from the class for cup 1: ", Chaicup.describe(cup)) # passing the reference to understand the context

cup_two = Chaicup() # Creating the object/instances
cup_two.size = 100 # Update the cup size for the object "cup_two"

print("Cup 2: ", cup_two.describe()) # Direct calling to method 
print("Direct from the class for cup 2: ", Chaicup.describe(cup_two)) # passing the reference to understand the context