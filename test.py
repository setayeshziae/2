import random

computer_number = (random.randint(10, 40))

x = 0

while 1 == 1:
    user_number = int(input("please enter a number:"))
    x = x + 1
    
    if computer_number == user_number:
       print("you win")
       break
       
    elif computer_number > user_number:
         print("go up")
        
    elif  computer_number < user_number:
          print("go down")
          
print("guess number = ", x)
          
          