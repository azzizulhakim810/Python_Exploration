flavors = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavor in flavors: 
  if flavor == "Out of Stock":
    continue
  if flavor == "Discontinued":
    break
  print(f"{flavor} item found")

print(f"Outside of loop!")