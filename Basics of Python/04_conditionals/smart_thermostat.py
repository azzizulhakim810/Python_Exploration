device_status = "active"
temperature = 38

if device_status == "active":
  if temperature > 35:
    print(f"High temperature alert!")
  else: 
    print(f"Temperature is normal")
else:
  print(f"Device is offline")