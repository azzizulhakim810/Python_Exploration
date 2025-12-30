#create a variable with integer value.
a=100
# print("The type of variable having value", a, " is ", type(a))
    
#create a variable with float value.
b=10.2345
# print("The type of variable having value", b, " is ", type(b))
    
#create a variable with complex value.
c=100+3j
# print("The type of variable having value", c, " is ", type(c))

# -------------------------------------------------------

a = "string in a double quote"
b= 'string in a single quote'
# print(a)
# print(b)
    
# using ',' to concatenate the two or several strings
# print(a,"concatenated with",b)

#using '+' to concate the two or several strings
# print(a+" concated with "+b)

# ---------------------------------------------------

#list of having only integers
a= [1,2,3,4,5,6]
# print(a)
    
#list of having only strings
b=["hello","john","reese", "cheese"]
# print(b)
    
#list of having both integers and strings
c= ["hey","you",1,2,3,"go", "down"]
# print(c)
    
#index are 0 based. this will print a single character
# print(c[1]) #this will print "you" in list c

# --------------------------------------------------

# tuple having only integer type of data.
a=(1,2,3,4)
# print(a) #prints the whole tuple
    
# tuple having multiple type of data.
b=("hello", 1,2,3, True)
# print(b) #prints the whole tuple
    
#index of tuples are also 0 based.
# print(b[4]) #prints the specific value from tuple

# -----------------------------------------------------

#a sample dictionary variable
    
a = {1:"first name",2:"last name", "age":33}
    
#print value having key=1
# print(a[1])
#print value having key=2
# print(a[2])
#print value having key="age"
# print(a["age"])

# -----------------------------------

# 1. Byte objects
data = b"hey"  # Immutable bytes object
mutable_data = bytearray(b"hey")  # Mutable bytearray object
view = memoryview(mutable_data)  # Memoryview of the bytearray

# 2. NumPy arrays
# import numpy as np

# Creating a 1D array
# data = np.array([1, 2, 3, 4])

# Creating a 2D array
# data_2d = np.array([[1, 2], [3, 4]])

# Performing element-wise operations
# squared = data ** 2

# ---------------------------------------------------

# Addition Operation +

addition = 8 + 3
# print("Addition:", addition)  # Output: 11

# Subtraction operation -
subtraction = 9 - 4
# print("Subtraction:", subtraction)  # Output: 5

# Multiplication operation *
multiplication = 10 * 2
# print("Multiplication:", multiplication)  # Output: 20

# Division operation /
division = 10 / 6
# print("Division:", division)  # Output: 1.6666666666666667

# Integer Division operation //
integer_division = 10 // 6
# print("Integer Division:", integer_division)  # Output: 1

# Modulus operation %
modulus = 10 % 6
# print("Modulus:", modulus)  # Output: 4

# Exponentiation operation **
exponentiation = 2 ** 6 # 2 * 2 * 2 * 2 * 2 * 2 
# print("Exponentiation:", exponentiation)  # Output: 64

# -----------------------------------------------------------

# Immutable Data Types 

sugar_amount = 2
# print(f"Initial Sugar: {sugar_amount}")


sugar_amount = 12
# print(f"Second Initial Sugar: {sugar_amount}")

# print(f"ID of 2: {id(2)}")
# print(f"ID of 12: {id(12)}")
# As their id is different from each other, so they are individual not same thing changing one 
# It creates a reference 


# Mutable Data Types 

spice_mix = set()
# print(f"Initial spice mix id: {id(spice_mix)}")
# print(f"Initial spice mix id: {(spice_mix)}")

spice_mix.add("Ginger")
spice_mix.add("Cardamom")

# print(f"Initial spice mix id: {id(spice_mix)}")
# print(f"Initial spice mix id: {(spice_mix)}")
# As they have the same id, so the same thing is changing after adding items


# -------------------------------------------------- 

total_tea_leaves_harvested = 1_000_000_000
# print("tea leaves:", total_tea_leaves_harvested)
# print(f"tea leaves: {total_tea_leaves_harvested}")


# Boolean ----------------------------------------------------

is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
# print(f"Total Actions: {total_actions}")

milk_presence = 0 # no milk
# print(f"Is there milk {bool(milk_presence)}")

# Logical ----------------------------------------------------

water_hot = True
tea_added = False

can_serve = water_hot and tea_added
can_serve_now = water_hot or tea_added
# print(f"Can serve the tea? {can_serve}")
# print(f"Can serve the tea now? {can_serve_now}")


# Real Number ----------------------------------------------------
import sys
ideal_temp = 95.5
current_temp = 95.499999999999999

# print(f"Ideal Temp {ideal_temp}")
# print(f"Current Temp {current_temp}")
# print(f"Difference Temp {ideal_temp - current_temp}")
# print(sys.float_info)


# String Type ----------------------------------------------------

chai_type = "Ginger Chai"
customer_name = "Jim"

# print(f"Order for {customer_name}: {chai_type} please !")

chai_description = "Aromatic and Bold"
# print(f"First Word: {chai_description[:8]}")
# print(f"Last Word: {chai_description[12:]}")
# print(f"Last Word: {chai_description[::-1]}")

label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")
decoded_label = encoded_label.decode("utf-8")

# print(f"Encoded Label: {encoded_label}")
# print(f"Decoded Label: {decoded_label}")


# Tuples, Membership ----------------------------------------------------

masala_spices = ("cardamom", "cloves", "cinnamon")

(spices1, spices2, spices3) = masala_spices

# print(f"Main masala spices are: {spices1, spices2, spices3}")

ginger_ratio, cardamom_ratio = 2, 1
# print(f"Ratio of G: {ginger_ratio} and Ratio of C: {cardamom_ratio}")

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
# print(f"Swapped Ratio of G: {ginger_ratio} and Swapped Ratio of C: {cardamom_ratio}")

# Membership 
# print(f"Is cinnamon in masala spices? {"cinnamon" in masala_spices}")


# Basic of List(Array) in Python ---------------------------------------------------------------------- 

ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar") # Adding new element from last
# print(f"Ingredients are: {ingredients}")

ingredients.insert(2, "sauce") # Adding new element in a specific position
# print(f"Ingredients are: {ingredients}")

ingredients.remove("black tea") # Eleminating the specific element
# print(f"Ingredients are: {ingredients}")

last_added = ingredients.pop() # Eleminating the last element
# print(f"Last element '{last_added}' removed from the {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
# print(f" chai: {chai_ingredients}")
chai_ingredients.reverse()
# print(f"Reverse the chai: {chai_ingredients}")

chai_ingredients.sort()
# print(f"Sorted chai: {chai_ingredients}")

sugar_level = [1, 2, 3, 4, 5]
# print(f"Maximum sugar level: {max(sugar_level)}")
# print(f"Minimum sugar level: {min(sugar_level)}")


# Operator Overloading & Bytearray in Python ---------------------------------------

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor # So the plus(+) outperform, it's not just a addition
# print(f"Liquid Mix: {full_liquid_mix}")

strong_brew = ["black tea", "Water"] * 3
# print(f"Strong Brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
# print(f"Bytes: {raw_spice_data}")



