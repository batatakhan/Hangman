import random
import sys

# Name: Areeb Ahmed Khan, UCID: 30130100

# The function "get_word" takes in a command line argument of a file and uses that to create a list of words with atleast 4 letters, it
# then randomly chooses a word out of that list and that is the secret word for the hangman.
# Parameters:
# 		None.
# Outputs:
# 		A randomly chosen word (with more than 3 letters) from the lexicon text file.

def get_word():
    
    file = open("lexicon.txt")
    line = file.readline()
    lexicon = []

    while line != "":
        line = line.rstrip()
        if len(line) >= 4:
            lexicon += [line]        
        line = file.readline()
  
    secret_word = random.choice(lexicon)
    file.close()

    return secret_word                 

# The function "convert" is just used to convert the list of either the "Bad guesses" or the "Secret word" into a string so it can
# be outputted to the screen in a good way.
# Parameters:
# 		The list that needs to be converted.
# Outputs:
# 		The list converted into a string followed by a space after each letter.

def convert(letter_list):
    
    output = ""
    for i in letter_list:
        output += i + " "

    return output
    
def hangman():
    
    word = get_word()
    dashes = ["_"] * len(word)
    bad_guesses = []
    guesses_left = 8

    print("Welcome to Console Hangman!\n\n")
    
    while guesses_left > 0 and "_" in dashes: # Conditions for the loop to break are only if you win or lose
        
        print("The secret word looks like: ", convert(dashes)) # Ex: _ _ _ _ _ or h e l _ o
        
        if len(bad_guesses) > 0:
            print("Your bad guesses so far:", convert(bad_guesses)) # Only displays when atleast one wrong guess has been made

        print("You have %d guesses remaining." %(guesses_left))
        
        while True:
            guess = input("What's your next guess? ").lower() # Converts to lowercase if letter entered is uppercase
            
            if len(guess) == 1: # Can only enter one letter at a time

                if guess.isalpha(): # Returns true if the guess is a letter (a-z) and false otherwise
                    
                    if guess in dashes or guess in bad_guesses: # Checks if the letter was guessed before
                        print("\nYou've already guessed this letter before, try again!")
                        continue
                
                    break # The loop only breaks when the guess is a single letter that is not guessed before

                else:
                    print("\nPlease only enter letters as guesses.")
                    continue

            else:
                print("\nYour guess must have exactly one character. ")

        if guess in word:
            
            index = 0
            for index in range(len(word)):
                letter = word[index] # Each index in the word is a letter
                if guess == letter:
                    dashes[index] = guess # All the dashes that satisfy get replaced by the correct guess 
                    index += 1
            
            print("Nice guess!\n")
            
        else:
            print('Sorry, there is no "%s".\n' %(guess))
            bad_guesses.append(guess)
            guesses_left -= 1

    # The loop can only break when you run out of guesses or when the word is guessed, so only need one condition for the
    # amount of guesses remaining to determine whether the game is won or lost.
    
    if guesses_left > 0:
        print("Congratulations!")
        print("You guessed the secret word:", word)
    
    else:
        print("You have no guesses remaining, better luck next time!")
        print("The secret word was:", word)


hangman()     
