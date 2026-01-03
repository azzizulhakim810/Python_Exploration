daily_sales = [3, 10, 8, 5, 9, 30, 15]


# Generator Comprehension =  (expression for item in iterable if condition (we can use other things like loops instead of condition)) - It's working fast as it's streaming & working. That's why we're putting sum in front of the expression
total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)

# [x for x in items] - make entire list in memory 
# (x for x in items) - like a stream