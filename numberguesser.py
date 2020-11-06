import random

print("Number Guessing Game")

number = random.randint(1, 9)

chances = 0

print("Guess a number between 1 and 9 :")

while chances < 5:

    
    guess = int(input("Guess and I'll tell you if it's correct:- "))


    if guess == number:
        print("Congratulation YOU WON!!!")

    elif guess < number:
        print("Your guess was too low : The correct number is a little higher!")

    else:
        print("Your guess was too high : The correct number is a little lower!")

    chances += 1

if not chances < 5:
    print("YOU LOSE!!! The number is", number)
