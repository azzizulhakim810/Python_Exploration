def update_order():
  chai_type = "Elachi"
  def kitchen():
    nonlocal chai_type
    chai_type = "Kesar"
    print(f"Inside the kitchen: {chai_type}")
  kitchen()
  print(f"Outside the kitchen: {chai_type}")
  

update_order()

