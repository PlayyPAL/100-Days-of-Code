rock = '''Rock\n
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''Paper\n
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''Scissors\n
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Setup
import random
choices = [rock, paper, scissors]
try:
    user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
except ValueError:
    print("Nope... Gotta type 0, 1, or 2 :)")
else:

#User
    if user >= 0 and user <= 2:
        print (f"You chose:\n {choices[user]}")

    #Computer
    bot = random.randint(0, 2)
    print(f"Computer chose: \n {choices[bot]}")

    #Result
    if user < 0 or user > 2:
        print("You chose.. Poorly. Did you read the instructions?")
    elif user == bot:
        print("It's a draw!")
    elif user == 0 and bot == 2:
        print("You win!")
    elif user == 0 and bot == 1:
        print("You lose!")
    elif user == 1 and bot == 0:
        print("You win!")
    elif user == 1 and bot == 2:
        print("You lose!")
    elif user == 2 and bot == 1:
        print("You win!")
    elif user == 2 and bot == 0:
        print("You lose!")
    else:
        print("Ummmmm...That's not quite how to do it.")