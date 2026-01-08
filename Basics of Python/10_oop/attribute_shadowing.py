class Chai:
  temperature = "hot"
  strength = "strong"


cutting = Chai()
print("Before Changing:", cutting.temperature)
cutting.temperature = "mild"
cutting.cup = "small" # Added attribute externally
print("Cup Size: ", cutting.cup)
print("After Changing: ", cutting.temperature)
print("Direct look into the Class: ", Chai.temperature)

del cutting.temperature
del cutting.cup

print("After Deletion: ", cutting.temperature) # This is the fallback. As I already delete the temperature from cutting object, then it's now used the parent class's temperature attribute

print(cutting.cup) # Shows Error --> AttributeError: 'Chai' object has no attribute 'cup'. After deletion, cup couldn't be found in the parent class as fallback