class Chai:
  origin = "Bangladesh"

print(Chai.origin)

Chai.is_hot = True
print("Chai Hot Status: ", Chai.is_hot)

masala = Chai()
print("Masala Original Country: ", masala.origin)
print("Masala Chai Hot Status: ", masala.is_hot)

masala.is_hot = False
print("Masala Chai Hot Status: ", masala.is_hot)
print("Chai Hot Status: ", Chai.is_hot)
