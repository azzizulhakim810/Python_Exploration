class Chaicup:
  size = 150

  # Creating method - function inside class is called method 
  def describe(self):
    return f"A {self.size}ml chai cup"
  
cup = Chaicup() # Creating the object/instances
print("Cup 1: ", cup.describe()) # Direct calling to method 
print("Direct from the class for cup 1: ", Chaicup.describe(cup)) # passing the reference to understand the context

cup_two = Chaicup() # Creating another object/instances
cup_two.size = 100 # Update the cup size for the object "cup_two"

print("Cup 2: ", cup_two.describe()) # Direct calling to method 
print("Direct from the class for cup 2: ", Chaicup.describe(cup_two)) # passing the reference to understand the context


# Simple analogy:
# Imagine self is like saying "myself" in real life:

# When you say "I'll describe myself," everyone knows you're talking about yourself
# When someone else says "Describe John," they need to specify who

# That's exactly what's happening:

# cup_two.describe() → "I (cup_two) will describe myself"
# Chaicup.describe(cup_two) → "Describe cup_two specifically"

# Both do the same thing, but the first way is more convenient because Python handles the self automatically!