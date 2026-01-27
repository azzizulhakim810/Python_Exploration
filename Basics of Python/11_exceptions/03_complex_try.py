def serve_chai(flavor):
  try:
    print(f"Preparing {flavor} chai...")
    if(flavor == "unknown"):
      raise ValueError("We don't know the flavor")
  except ValueError as ve:
    print(f"Error: {ve}")
  else:
    print(f"{flavor} chai is ready to be served!")
  finally:
    print("Thank you for visiting our chai shop!")


serve_chai("masala") 
serve_chai("unknown") 