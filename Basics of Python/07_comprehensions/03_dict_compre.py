# Dictionary - key:value 
tea_prices_bdt = {
  "Masala Chai": 30,
  "Green Tea": 80,
  "Lemon Tea": 200
}
                              # That expression should be key:value
# Dictionary Comprehension =  {expression for item in iterable if condition (we can use other things like loops instead of condition)} 

# Using {}

tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_bdt.items()}
print(tea_prices_usd)
