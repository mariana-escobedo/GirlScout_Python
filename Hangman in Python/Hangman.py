import random
from list import listy
from stickman import updateGame, replaceLetters, gameState


###PART 1: Lists and Variables
### You will need to start adding your variables here.
### Here is a list of the variables you will need to get your game started! :)
### HINT: Refer to your cheat sheet for help!
### 
### secret_word  (string)
### guessed (list)
###chances = 5
### wrongs (int)
### guess (string)

secret_word = "food"
chances = 5
guessed = []
wrongs = 0
guess = "" 
L = ["_" for i in range(0, len(secret_word))]

##GAME START!
print("★ Welcome to Hangman! ★ \n﻿")


while True:
    print("Chances: " + str(chances))
    
###PART 2: Inputs and Outputs
### Here you show the player the start of the game.
        #-> print your 'known' array
        #-> print your 'guessed' variable
    updateGame(chances)
    
    
    #Get their one letter guess (hint: input)
    inp = input("\n >> ")


###PART 3: If Statements and Conditions
    #check IF the player already guessed that letter
    
        #if they did: print out a statement telling them
        
    
    #IF they didn't: update the guessed list by adding their guess to it.(HINT: .append() )
        
        
    #then check if they guessed it right or wrong. (Is the user input inside the secret_key?)
        #if RIGHT => update the secret word list
    
        #if WRONG => bump their chances variable down by 1 point
    
            

    #check if player won yet (are there any _ left inside of 'known'?)
    if (''.join(L) == secret_word):
        print("\n Known:" + str(L)+ "      Guessed:" + str(guessed))
        print("Chances" + chances)
        #congrats message 
        break

    elif ( ''.join(L) != secret_word and (chances ==0)):
        updateGame(chances)
        print("\n Known:" + str(L)+ "      Guessed:" + str(guessed))
        #lost message 
        break
    
    else:
        continue 







