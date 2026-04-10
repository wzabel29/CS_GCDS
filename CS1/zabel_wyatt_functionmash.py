import time
def chorus():
    print("""Jealousy
Turning saints into the sea
Swimming through sick lullabies
Choking on your alibis
But it's just the price I pay
Destiny is calling me
Open up my eager eyes
Cause Im Mr. Brightside
""")

def sing_song():
    print("""Comin' out of my cage and I've been doin' just fine
Gotta, gotta be down because I want it all
It started out with a kiss, how did it end up like this?
It was only a kiss, it was only a kiss
Now I'm falling asleep and she's calling a cab
While he's having a smoke and she's taking a drag
Now they're goin' to bed and my stomach is sick
And it's all in my head, but she's touching his

Chest now
He takes off her dress now
Let me go
And I just can't look, it's killing me
And taking control
""")
    time.sleep(1)
    chorus()
sing_song()

def add():
    def get_number(order):
        try:
            num = int(input(f"pick your {order} number:"))
        except ValueError:
            print("please enter a valid number")
        if num > 0:
            return num
        
    num_1 = get_number("first")
    num_2 = get_number("second")
    return num_1 + num_2
print(add())