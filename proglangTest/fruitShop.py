#  Fruit Shop Price Lookup BEGINNER
# Dictionaries Key-Value Pairs A grocery store manages item prices in a Python dictionary.
# fruit_prices = { "Apple": 2.5, "Banana": 1.0, "Mango": 3.0, "Orange": 1.5 }
# Add a new fruit "Grapes" priced at 2.0 to the dictionary.
# Update the price of "Banana" to 1.2.
# Write a loop to print each fruit name along with its price in a clean line.


fruit_prices = { "Apple": 2.5, "Banana": 1.0, "Mango": 3.0, "Orange": 1.5 }

# Add "Grapes" priced at 2.0
fruit_prices["Grapes"] = 2.0

# Update price of "Banana" to 1.2
fruit_prices["Banana"] = 1.2

# Loop to print each fruit name along with its price
for fruit, price in fruit_prices.items():
    print(f"{fruit}: ${price}")