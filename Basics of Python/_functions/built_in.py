def chai_flavor(flavor="masala"):
  """Return the flavor of Chai"""
  chai="Ginger"
  return flavor

# print(chai_flavor("Garam"))
print(chai_flavor.__doc__) # it prints only the first line(doc) after defining the function
print(chai_flavor.__name__) # it prints the name of the function

def generate_bill(chai=0, samosa=0):
  """
  Calculate the total bill for chai & samosa
  
  :param chai: Number of chai cups (10tk each)
  :param samosa: Number of samosa (15tk each)
  : return: (total amount, thank you messge as string)

  """

  total = chai*10 + samosa*15
  return total, "Thank you for visiting us"

final_bill = generate_bill(2, 5)
print("Final Bill:", final_bill)