# 3 condition for user to win
# rock paper scissor game

import random
random_num = random.randint(1,10)
print("Enter your choice:")
print("1 = Rock")
print("2 = Paper")
print("3 = Scissors")

while True:
    number = int(input("choose a number"))
    random_num = random.randint(1,3)
    choice_name = {
    "1":"Rock",
    "2":"Paper",
    "3":"Scissors"
}
    if number == random_num:
        print("It's a tie:")
    elif (number == 1 and random_num == 2) or (number == 2 and random_num == 3) or (number == 3 and random_num == 1):
        print("You loose! Better luck next time")
    else:
        print("Congrats! You won the game")

    user = input("Do you want to play again? y/n ").lower()
    if user != "y":
        print("Thank you for playing!")
        break



    
    
