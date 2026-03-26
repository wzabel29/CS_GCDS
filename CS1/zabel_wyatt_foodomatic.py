import random

mains = ["Atlantic salmon served on a bed of wild rice","Burger with Truffle Fries ","Halibut Piccata", "Chicken Picatta","potatoe Gnocci","three color squash Rissoto", "eggplant parm", "Tomahawk steak","escargo with baguette"]
prices = int["20", "25", "28", "30", "18", "20", "22", "30", "20"]
flairs = ["with balsamico","with garlic and olive oil","with minted yogurt","with chutney","with a salad", "with salsa", "over sticky rice","au jus", "with basmati rice"]
flair_prices = int["3", "4", "5", "5", "7", "4", "4", "6", "5"]
user_items = int(input('How many items do you need?'))

for i in range(user_items):
    main = random.choice(mains)
    flair = random.choice(flairs)
    index_main = mains.index(main)
    index_flair = flairs.index(flair)
    final_price = flair_prices[index_flair] + prices[index_main]

    print(f"{main} is ${prices[index_main]} with {flair} which costs ${flair_prices[index_flair]}. The total price for your meal is ${final_price}.")

# print(f"The final price for your meal is ${Meal_Price}")

