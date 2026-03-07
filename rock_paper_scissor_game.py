import random
item_list=["Rock","Paper","Scissor"]
user_choice=input("Enter your move Rock,Paper,Scissor:")
computer_choice=random.choice(item_list)
print("Your move is",user_choice)
print("Computer's move is",computer_choice)

if(user_choice==computer_choice):
    print("Match has tied")
elif(user_choice=="Rock" and computer_choice=="Paper" ):
    print("Computer has won")
elif(user_choice=="Rock" and computer_choice=="Scissor" ):
    print("You have won")
elif(user_choice=="Paper" and computer_choice=="Rock" ):
    print("You have won")
elif(user_choice=="Paper" and computer_choice=="Scissor" ):
    print("Computer has won")
elif(user_choice=="Scissor" and computer_choice=="Paper" ):
    print("You have won")
elif(user_choice=="Scissor" and computer_choice=="Rock" ):
    print("Computer has won")
else:
    print("Invalid input")










    
