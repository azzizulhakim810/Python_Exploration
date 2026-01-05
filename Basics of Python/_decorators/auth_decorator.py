from functools import wraps

def requier_admin(func):
  @wraps(func)
  def wrapper(user_role):
    if user_role != "admin":
      print("Access Denied: Admins Only")
      return None # default return. Without this like is okay
    else:
      return func(user_role)
  return wrapper
    
@requier_admin
def access_tea_inventory(role):
  print("Access Granted to the Tea Inventory; Role: ",role)

access_tea_inventory("user")
access_tea_inventory("admin")