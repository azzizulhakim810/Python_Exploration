staffs = [("Semmon", 25), ("Hridoy", 27), ("Saiful Bhai", 29), ("Rez", 26), ("Kowshik", 26)]

for name, age in staffs:
  if age >= 22:
   print(f"{name} is eligible to manaage the staff")
   break

else: # It's kind a fallback -- if it won't break, then this wouldn't be printed
  print(f"None is eligible to manage the staff")