print("Welcome to the quiz Game! ")

playing = input("do you want to play?\n:-") 

if playing.lower() == "yes":
    print("Okay! Let's play :)")
else:
    print("Maybe next time!")
    exit()
score = 0

answer = input("What does CPU stand for?\n:-")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Central Processing Unit.")

answer = input("What does GPU stand for?\n:- ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Graphics Processing Unit.")

answer = input("What does RAM stand for?\n:- ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Random Access Memory.")

answer = input("What does ROM stand for?\n:- ")
if answer.lower() == "read-only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Read-Only Memory.")

print(f"You got {score} questions correct!")
print(f"you got {score}/4 questions correct, which is {score/4*100:.2f}%")