import random

user_score = 0
computer_score = 0
computer_choice = random.choice(['rock', 'paper', 'scissors'])
if __name__ == "__main__":
    user_choice = input("Type 'rock', 'paper', or 'scissors' to play (or 'quit') to exit\n:").lower()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if user_choice == 'quit':
        print("Thanks for playing!")
        break
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        continue
    
    #rock beats scissors, scissors beats paper, paper beats rock.
    if user_choice == computer_choice:
        print(f"Both choices are {user_choice}.\n It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors'):
        print("You win!")
        user_score += 1
    elif (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        user_score += 1
    elif (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1
    print("\n" + "=" * 32)
    print("          FINAL SCORE")
    print("=" * 32)
    print(f"  You      : {user_score}")
    print(f"  Computer : {computer_score}")
    print("=" * 32)
    if user_score > computer_score:
        print("       YOU ARE THE CHAMPION!")
    elif computer_score > user_score:
        print("        COMPUTER WINS!")
    else:
        print("          IT'S A TIE!")
    print("=" * 32)