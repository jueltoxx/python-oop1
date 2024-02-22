import random

list = ["rock","paper","scissors"]

player1 = list[random.randint(0,2)]
player2 = list[random.randint(0,2)]

if player1 == player2:
    print("Draw!")
elif player1 == "rock" and player2 == "scissors" or player1 == "scissors" and player2 == "paper" or player1 == "paper" and player2 == "rock":
    print("player1 wins!")
else:
    print("player2 wins!")

print()
print("Player1 uses: ",player1)
print("player2 uses: ",player2)