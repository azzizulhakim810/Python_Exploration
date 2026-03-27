from pydantic import BaseModel

class Product(BaseModel):
  id: int
  name: str
  price: float
  in_stock: bool = True


product_one = Product(id= 1, name="Laptop", price= 20.49, in_stock= True)

product_two = Product(id=2, name="Mouse", price= 89) # in_stock True for all automatically

# product_three = Product(name= "Keyboard") # Throws error as there is no id, price [in_stock built in True for all]

print(product_one, product_two)


# pydantic automatically do -> 
# "20" -> 20 if type is int
# "True" -> True if type is bool
# 20 -> 20.0 if type is float
