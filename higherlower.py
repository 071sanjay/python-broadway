

import random
random_number = random.randint(1,10)
print("random number is: ", random_number)
count = 0
attempts = 5

while True:
    if count>attempts - 1:
        input("No attempts left")
        user = input("do you want to continue y/n").lower()
        if user == "y":
             random_number = random.randint(1,10)
             print(f'random number is: {random_number}' )
        else:
             print("thank you for playing")
        break
    print(f'remaining attempts: {attempts - count}')

    count = count+1
    user = int(input("Guess a number"))
    if count == random_number:
        print("Guessed successfully")
        break
    if user>random_number:
        print("little low")
    elif user<random_number:
        print("little high")
    elif user != random_number:
        print("attempt left:", count)
else:
        print("try again")













