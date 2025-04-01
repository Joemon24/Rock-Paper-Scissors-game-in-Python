import random

player = int(input("Choose your number (0 for rock, 1 for paper or 2 for scissors): "))

computer = random.randint(0, 2)

if player == computer:
    print("It's a tie!")
elif player == 0 and computer == 1:
    print("You lose! Paper beats rock")
elif player == 0 and computer == 2:
    print("You win! Rock beats scissors")
elif player == 1 and computer == 0:
    print("You win! Paper beats rock")
elif player == 1 and computer == 2:
    print("You lose! Scissors beats paper")
elif player == 2 and computer == 0:
    print("You lose! Rock beats scissors")
elif player == 2 and computer == 1:
    print("You win! Scissors beats paper")
else:
    print("Invalid input! Please choose 0, 1, or 2")