cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "small":
  print(f"Price is 10tk")
elif cup == "medium":
  print(f"Price is 15tk")
elif cup == "large":
  print(f"Price is 20tk")
else:
  print(f"Unknown cup size")