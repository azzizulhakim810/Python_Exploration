# Pure Function --------------------------------------
def pure_chai(cups):
  return cups * 2

print(pure_chai(3))


# Impure Function --------------------------------------
total_chai = 0

def impure_chai(cups):
  global total_chai
  total_chai += cups

impure_chai(3)
print("Total Chai: ", total_chai)


# Recursive Function --------------------------------------
def pour_chai(n):
  print(n)
  if n==0:
    return "All coups are poured"
  return pour_chai(n-1)

print(pour_chai(3))


# Lambda/Annonymous Function --------------------------------------

chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))

print(strong_chai)