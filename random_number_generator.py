import random
top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()
random_number = random.randint(-1, int(top_of_range))
print(f"Random number: {random_number}")

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_number:
            print("Congratulations! You guessed the number.")
            break
        else:
            print("Incorrect guess. Try again.")
    else:
        print("Please type a number next time.")
        continue
    if user_guess < random_number:
        print("your guess is too low.")
    elif user_guess > random_number:
        print("your guess is too high.")
    else:
        print("You missed the number. The correct number was", random_number)
        break

print("Thanks for playing!")