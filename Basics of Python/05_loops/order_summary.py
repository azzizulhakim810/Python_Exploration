names = ["Saiful Bhai", "Semmon", "Sagor Bhai", "Kowshik", "Hridoy", "Adnan", "Rez"]
bills = [1000, 1400, 300, 500, 800, 400, 700]

for name, amount in zip(names, bills):
  print(f"{name} paid {amount}tk")