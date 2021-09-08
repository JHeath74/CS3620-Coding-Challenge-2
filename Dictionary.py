#Part 4

productDictionary =	{
  "Banana": "15",
  "Raspberry": "20",
  "Beef Jerky": 25,
  "Strawberry": "30",
  "Fish": "35",
  "Marshmellows": 40,
}

prodic = str(list(productDictionary.keys()))

product = input("Type a product name from the list: " + prodic + ":");

print(product)
print(product + " is " + productDictionary[product] + " Dollars")