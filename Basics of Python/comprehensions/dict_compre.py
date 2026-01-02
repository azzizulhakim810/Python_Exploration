# Dictionary - key:value 
tea_prices_bdt = {
  "Masala Chai": 30,
  "Green Tea": 80,
  "Lemon Tea": 200
}

tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_bdt.items()}
print(tea_prices_usd)
