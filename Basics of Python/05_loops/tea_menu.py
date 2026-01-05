menu = ["Green", "Lemon", "Spiced", "Mint"]

for idx, item in enumerate(menu, start=1):
  print(f"{idx}: {item}")

print(f"{list(enumerate(menu, start=1))}")