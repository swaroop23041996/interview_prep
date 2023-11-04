import random
jackpot_num=random.randint(1,100)
num=int(input("Enter any number between 1 -100  "))
count=1
while num!=jackpot_num:
    if num < jackpot_num:
        print("Your number is smaller than Jackpot number")
        num=int(input("Try with another number  "))
        count=count+1
    else :
        print("Your number is larger than Jackpot number")
        num=int(input("Try with another number  "))
        count=count+1
print("you choose the correct number")
print("You took ",count," attempt")
