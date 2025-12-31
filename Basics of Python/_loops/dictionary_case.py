users = [
  {"id": 1, "total": 800, "coupon": "P40"},
  {"id": 2, "total": 400, "coupon": "C80"},
  {"id": 3, "total": 100, "coupon": "E10"}
]

discounts = {
  "P40": (0.4, 0),
  "C80": (0, 80),
  "E10": (0.1, 0)
}

for user in users:
  percent, fixed = discounts.get(user["coupon"], (0, 0))
  discount = user["total"] * percent + fixed

  print(f"{user["id"]} paid {user["total"]} and got discount for next visit of {discount}tk")
