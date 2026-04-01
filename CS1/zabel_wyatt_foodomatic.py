import random

mains = ["Spicy salmon roll","Chicken fried rice","Pork lo mien", "Spicy tonkutsu ramen","Chicken and brocoli","Crab soup dumplings", "Pan fried pork dumplings", "Tuna and avocado roll","Shrimp tempura roll"]
main_prices = [20, 25, 28, 30, 18, 20, 22, 30, 20]
flairs = ["with spicy edemamme","with soy sauce and spicy mayo","with crab rangoons","with white rice","with seaweed salad", "with miso soup", "with vegetable springrolls","with spicy cucumbers", "with egg drop soup"]
flair_prices = [3, 4, 5, 5, 7, 4, 4, 6, 5]
while True:
    try:
     user_items = int(input('How many items do you need?'))
     break
    except ValueError:
      print("Please enter a valid number.")
      continue

total = 0

for i in range(user_items):
    main = random.choice(mains)
    flair = random.choice(flairs)
    index_main = mains.index(main)
    index_flair = flairs.index(flair)
    final_price = (flair_prices[index_flair]) + (main_prices[index_main])
    total += final_price
    print(f"{main} is ${main_prices[index_main]} {flair} which costs ${flair_prices[index_flair]}. The total price for your meal is ${final_price}.")

print(f"The final price for your meal is ${total}")