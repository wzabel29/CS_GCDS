import random

mains = ['cauliflower','tilapia fillet', 'pork loin', 'salmon', 'potatoes', 'three color squash', 'eggplant', 'steak','baguette']
prices = ["$20", "$25", "$28", "$30", "$18", "$20", "$22", "$30", "$20"]
flairs = ["with balsamico","with garlic and olive oil","with minted yogurt","with chutney","salad", "with salsa", "over sticky rice","au jus", "with basmati rice"]

user_items = int(input('How many items do you need?'))

for i in range(user_items):
    main = random.choice(mains)
    flair = random.choice(flairs)
    index = mains.index(main)
    print(f"{main} {flair} is {prices[index]}.")