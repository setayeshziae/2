import random 
print("enjoy this game")

while 1==1:
    d =input("roll the dice:")
    dice = random.randint(1, 6)
    print(dice)

    if dice == 6:
        ("great, roll the dice again")
    
    else: 
        print("sorry, you lost")
        break
    