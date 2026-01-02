# def make_chai():
#   return "Here is the masala chai"

# # print(make_chai())
# return_value = make_chai()
# print(return_value)

# Return one value ---------------------------------------

def idle_chaiwala():
  pass

# print(idle_chaiwala())

def sold_cups():
  return 200

total = sold_cups()
# print(total)

# Early Return ---------------------------------------

def chai_status(cups_left):
  if cups_left == 0:
    return "Sorry, chai over"
  return "Chai is ready"
  print("Chai")

print(chai_status(0))
print(chai_status(5))

# Return more value  ---------------------------------------

def chai_report():
  return 40, 20, 80 #sold, remaining

sold, remaining, _ = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)