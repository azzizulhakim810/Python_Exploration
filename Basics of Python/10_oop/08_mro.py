# Method Resolution Order 
class A:
  label = "A: Base Class"

class B(A):
  label = "B: Masala Class"

class C(A):
  label = "C: Herbal Class"

class D(B, C): # Whichever comes first in the bracket(), that class will be executed
  pass

cup = D()
print(cup.label)
print(D.__mro__) # Shows the sequence where it comes from