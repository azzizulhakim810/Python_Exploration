snack = input("Enter your prefered snack: ").lower()

if snack == "cookies" or snack == "samosa": # snack == "cookies" or "samosa" --> not working
  print(f"Great Choice! We'll serve {snack} very soon")
else:
  print(f"Sorry! We only serve 'Cookies' and 'Samosa' today")