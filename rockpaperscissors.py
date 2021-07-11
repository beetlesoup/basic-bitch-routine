
from random import randint

def play_verifier(play):
    """this function is so the player can enter more than one possible
    value, and the programmer can act like they only recieve the
    cleanest of data entries. Would you call this an elegant solution?
    For a noob, at least."""

    hand = ["Rock", "Paper", "Scissors"]

    while play not in hand:

        if play.lower()[0] == "r" or play[0] == 1:
            play = "Rock"
        elif play.lower()[0] == "p" or play[0] == 2:
            play = "Paper"
        elif play.lower()[0] == "s" or play[0] == 3:
            play = "Scissors"

        else:
            play = input("Bad entry, bucko. R, P, S?")

    player = play
    return player, hand




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
