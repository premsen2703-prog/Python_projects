import random

user_score = 0
computer_score = 0

while True:
    user_choice = input("Type 'rock', 'paper', or 'scissors' to play (or 'quit') to exit\n:").lower()
    if user_choice == 'quit':
        print("Thanks for playing!")
        break
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        continue
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    #rock beats scissors, scissors beats paper, paper beats rock.
    if user_choice == computer_choice:
        print(f"Both choices are {user_choice}. It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors'):
        print(f"You chose {user_choice} and the computer chose {computer_choice}. You win!")
        user_score += 1
    elif (user_choice == 'scissors' and computer_choice == 'paper'):
        print(f"You chose {user_choice} and the computer chose {computer_choice}. You win!")
        user_score += 1
    elif (user_choice == 'paper' and computer_choice == 'rock'):
        print(f"You chose {user_choice} and the computer chose {computer_choice}. You win!")
        user_score += 1
    else:
        print(f"You chose {user_choice} and the computer chose {computer_choice}. You lose!")
        computer_score += 1

print(f"Final score - You: {user_score}, Computer: {computer_score}")