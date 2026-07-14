import random

computer_number = random.randint(1, 50)


chance = 5

while chance > 0:
    user_guess = int(input("Enter a number between 1 and 50: "))
    if user_guess < computer_number:
        print("Your guess is too low.")
    elif user_guess > computer_number:
        print("Your guess is too high.")
    else:
        print("Congratulations! You guessed the correct number.")
        break
    chance -= 1
else:
    print("Sorry ,You have ran out of chances. The correct number was", computer_number)
    