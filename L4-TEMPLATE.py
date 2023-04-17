'''

NAME:   PUT YOUR NAME HERE

DATE:   DATE OF YOUR SUBMISSION

ASSN:   LAB ASSIGNMENT L3

DESC:   THE FOLLOWING PYTHON MODULE IMPLEMENTS THE FAMOUS ROCK,
        PAPER, SCISSORS GAME.  THE RULES OF THE GAME ARE SIMPLE.
        EACH PLAYER CHOOSES A ROCK (0), PAPER(1), OR SCISSORS (2).
        THE FOLLOWING ARE WINNING PLAYS:
        
        ROCK BEATS SCISSORS
        PAPER BEATS ROCK
        SCISSORS BEATS PAPER

'''

# COMPUTER CHOOSES ROCK, PAPER, OR SCISSORS BASED ON A RANDOM
# INTEGER CHOICE USING THE RANDINT() FUNCTION.
from random import randint
computer_choice = randint(0,2)

# GET THE USER CHOICE, user_choice, USING THE input() function
# AS AN INTEGER
rock = 0
paper = 1
scissors = 2
user_choice = int(input("Select an action through 1 and 3: "))


# IMPLEMENT THE RULES OF THE GAME USING IF-ELIF-ELSE STATEMENTS

if user_choice == 0 and computer_choice == 2:
    print ("Player 1 wins they chose " + str(0))
elif user_choice == 1 and computer_choice == 0:
    print ("Player 1 wins they chose " + str(1))
elif user_choice == 2 and computer_choice == 1:
    print ("Player 1 wins they chose " + str(2))
elif user_choice == computer_choice:
    print("Tie")
else :
    print("The computer won they chose " + str(computer_choice))
    if computer_choice == 0:
        print("Rock")
    if computer_choice == 1:
        print("Paper")
    if computer_choice == 2:
      print("Scisorrs")








# IF PLAYER 1 CHOOSES ROCK AND PLAYER 2 CHOOSES SCISSORS, OR
# IF PLAYER 1 CHOOSES PAPER AND PLAYER 2 CHOOSES ROCK, OR
# IF PLAYER 1 CHOOSES SCISSORS AND PLAYER 2 CHOOSES PAPER, THEN
# PLAYER 1 WINS
#
# ELSE IF PLAYER 1 AND PLAYER 2 CHOOSES THE SAME OBJECT, THEN
# IT'S A TIE
#
# OTHERWISE, PLAYER 2 WINS



# PRINT THE WINNER AND THEIR CHOICE


###############
### THE END ###
###############


