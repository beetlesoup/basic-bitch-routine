
from random import randint

hand = ["Rock", "Paper", "Scissors"]

computer = hand[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors?")


player = False
computer = hand[randint(0,2)]
