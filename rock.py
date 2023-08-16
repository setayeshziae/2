import random 

computer_concession  = 0 
user_concession = 0 

print("welcome")
print("you can use 🗿, 📃, ✂️ emojis")

while computer_concession < 5 and user_concession < 5:
    x = random.randint(1, 3)
    
    if x == 1:
        computer_choice = "🗿"
    elif x == 2:
        computer_choice = "📃"
    elif x == 3: 
        computer_choice = "✂️"
        
    user_choice = input()
    
    print("🤖", computer_choice)
    print("👩🏻", user_choice)
    
    if computer_choice == "🗿" and user_choice == "📃":
       user_concession = user_concession + 1 
       
    elif computer_choice == "🗿" and user_choice == "✂️":
         computer_concession = computer_concession = 1
         
    elif computer_choice == "✂️" and user_choice == "📃":
         computer_concession = computer_concession + 1
         
    elif computer_choice == "✂️" and user_choice == "🗿":
        user_concession = user_concession +1
        
    elif computer_choice == "📃" and user_choice == "🗿":
        computer_concession = computer_concession + 1 
        
    elif computer_choice == "📃" and user_choice == "✂️":
        user_concession = user_concession +1
        
    elif computer_choice == "🗿" and user_choice == "🗿":
        computer_concession = computer_concession + 0 
        
    elif computer_choice == "📃" and user_choice == "📃":
        computer_concession = computer_concession +0
        
    elif computer_choice == "✂️" and user_choice == "✂️":
        computer_concession = computer_concession + 0
        
    print ("computer concession is:", computer_concession)
    print ("user concession is:", user_concession)
        