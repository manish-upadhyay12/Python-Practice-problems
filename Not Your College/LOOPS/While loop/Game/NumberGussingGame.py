# Question : This is a number gussing game where you will choose randam number and your step will be count , according to step you will gain award
# so try to choose number in  few step 
import random
number = random.randint(1, 100)    # computer choose random number

step = 0  # count ,use for count step of player
while (step<15):   # condition will false when candidate choose right number
    choose = int(input("Guess number ,and try to chcoose right number :"))
    step += 1
    if choose > number:
        print("Too high! Go down.")

    elif (choose < number):
        print("Too low! Go up.")

    else:
        # candidate choose write number and loop will be end
        print("congratulation !you won the game")
        break

# decide position and award according to step 
if step <= 5:   # check for 1st position
    print("1st positiion")
    print(f"you win this game in {step} steps ")
    print("you winbike")

elif (step > 5 and step <= 9):    # check for 3rd position

    print("2nd positiion")
    print(f"you win this game in {step} steps ")
    print("you win cycle")
elif (step > 9 and step <= 13):   # check for 2nd position

    print("3rd positiion")
    print(f"you win this game in {step} steps ")
    print("you win phone")
else:
    print("you dont won anything "" : ""Game over")


print("Thanks for playing ")
