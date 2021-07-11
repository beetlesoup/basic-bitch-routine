
from random import randint
from random import choice

def play_verifier(play):
    """this function is so the player can enter more than one possible
    value, and the programmer can act like they only recieve the
    cleanest of data entries. Would you call this an elegant solution?
    For a noob, at least."""

    if play.lower()[0] == "r" or play[0] == 1:
        play = "Rock"
    elif play.lower()[0] == "p" or play[0] == 2:
        play = "Paper"
    elif play.lower()[0] == "s" or play[0] == 3:
        play = "Scissors"

    player = play
    return player

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

score = 0
hand = ["Rock", "Paper", "Scissors"]
comments = ["Interesting choice.",
            "Why would you do that?",
            "Do you like that move?",
            "Are you proud of that choice?"]
crowd = ["BOOOOOOOOO!",
         "Yeeeeaaaaahhhhhhhh",
         "Lukewarm"]

player = False

while player == False:
    computer = hand[randint(0,2)]
    player = input("Rock, Paper, Scissors? ")

    while player not in hand:
        player = play_verifier(player)
        while player not in hand:
            player = input("Don't mess with me. R, P, S? ")
            player = play_verifier(player)

    print("You chose: {}. {}".format(player.upper(), choice(comments)))
    print("Computer chose: {}.".format(computer.upper()))

    if player == computer:
        print("Curious. Why did you choose the same thing?".format(computer))

    elif player == "Rock":
        if computer == "Paper":
            print("You lose. Computer wraps you up tight.")
            score -= 1
        else:
            print("You win! You smash computer. Ow.")
            score += 1

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose. Computer cuts you.")
            score -= 1
        else:
            print("You win! You cover computer. Go work out.")
            score += 1

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose. Computer smashes you.")
            score -= 1
        else:
            print("You win! You cut computer.")
            score += 1

    print("SCORE: ", score)

    yallah_tani = input("Play again? ")

    while yallah_tani.lower()[0] == "y":
        player = False

    else:
        print("Okay. See you again.")
