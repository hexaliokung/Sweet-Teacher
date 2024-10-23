# Shoping cart program

FOODS = []
PRICES = []
TOTAL = 0

while True:
    FOOD = input("Enter a food to buy (q to quit): ")
    if FOOD.lower() == "q":
        break
    else:
        PRICE = float(input(f"Enter the price of a {FOOD}: $"))
        FOODS.append(FOOD)
        PRICES.append(PRICE)

print("----- YOUR CART -----")

for FOOD in FOODS:
    print(FOOD, end=" ")

for PRICE in PRICES:
    TOTAL += PRICE

print(f"Your total is ${TOTAL}")