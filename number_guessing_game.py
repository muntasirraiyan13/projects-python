import random
number=random.randint(1,101)
attempt=0
while True:
    guess=int(input("Input a number between 1 to 101:"))
    attempt=attempt+1
    if(guess<number):
        print("Too low.Try again!")
    elif(guess>number):
        print("Too High.Try again!")
    else:
        print("Congraculations!You have guessed the right number in", attempt,"attempts")
        break
    
