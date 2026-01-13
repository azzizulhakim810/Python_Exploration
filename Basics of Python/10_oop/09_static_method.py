class ChaiUtils:
  @staticmethod # after adding this decorator we can access to direct parent, no need to create object
  def clean_ingredients(text):
    return [item.strip() for item in text.split(",")]
  
raw_text = "water,  milk,     ginger, honey"

# obj = ChaiUtils()
# cleaned = obj.clean_ingredients(raw_text)

cleaned = ChaiUtils.clean_ingredients(raw_text)
print(cleaned)