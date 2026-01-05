def serve_chai():
  chai_type = "Masala" # local Scope
  print(f"Inside function: {chai_type}")

chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}")


def chai_counter():
  chai_order = "Lemon" # Enclosing Scope
  def print_order():
    chai_order = "Ginger"
    print(f"Inner: {chai_order}")
  print_order()
  print(f"Outer: {chai_order}")

chai_order = "Tulsi" # Global
chai_counter()
print(f"Global: {chai_order}")