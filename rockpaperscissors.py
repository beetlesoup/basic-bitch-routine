
from random import randint

def play_verifier(play):
    """this function is so the player can enter more than one possible
    value, and the programmer can act like they only recieve the
    cleanest of data entries. Would you call this an elegant solution?
    For a noob, at least."""
    
    if player.lower()[0] == "r" or "1":
        player = "Rock"
    elif player.lower()[0] == "p" or "2":
        player = "Paper"
    elif player.lower()[0] == "s" or "3":
        player = "Scissors"

    return player



hand = ["Rock", "Paper", "Scissors"]

computer = hand[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors?").lower()

    if player in names:


        if player == computer:
            print("Computer played {}. Curious. Why did you choose the same thing?".computer)
        elif player

    else player = input("Bad entry, bucko. R, P, S?")

    player = False
    computer = hand[randint(0,2)]
