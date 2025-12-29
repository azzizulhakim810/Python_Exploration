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
b=("hello", 1,2,3,"go")
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
integer_division = 10 // 2
# print("Integer Division:", integer_division)  # Output: 5

# Modulus operation %
modulus = 10 % 5
# print("Modulus:", modulus)  # Output: 0

# Exponentiation operation **
exponentiation = 2 ** 6
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
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix id: {(spice_mix)}")

spice_mix.add("Ginger")
spice_mix.add("Cardamom")

print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix id: {(spice_mix)}")
# As they have the same id, so the same thing is changing after adding items
