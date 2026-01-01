def add_vat(price, vat_rate):
  return price * (100 + vat_rate) / 100

orders = [100, 120, 150]

for bill in orders:
  final_amount = add_vat(bill, 10)
  print(f"Original: {bill}, Final_with_VAT: {final_amount}")