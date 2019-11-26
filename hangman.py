import random
    
def get_guess():
    #Set dashes to length equal to the length of the secret word
    dashes = "-" * len(secret_word)
    
    #let guesses_left equal to 10
    guesses_left = 10
    
    #This loop runs if two conditions are true:
    #1. No. of guesses left is greater than -1
    #2. The dash string is not equal to secret word
    while guesses_left > -1 and not dashes == secret_word:
        print(dashes)
        print(guesses_left)
        
        #Ask for user input
        guess = input("Input a letter:")
        
        #Conditions that will print out a message
        #according to invalid inputs
        if len(guess) != 1:
            print("ALERT! you must enter one Letter!")

        #If the letter is in the secret word
        #replace the dash with that letter in the
        #Correct index
        elif guess in secret_word:
            print("Great! The letter is in the secret word!")
            dashes = update_dashes(secret_word,dashes,guess)
            
        #If the user guess is wrong , Display message
        # the user's guess count dcrease by 1
        else:
            print("Sorry! The letter is not in the secret word!")
            guesses_left -= 1
    
    if guesses_left < 0 :
        print("You LOSE. The word was: " + str(secret_word))
    
    else:
        print("Congrats! You win. The word was: " + str(secret_word))
        


def update_dashes(secret,cur_dash, rec_guess):
    result = ""
    
    for i in range(len(secret)):
        if secret[i] == rec_guess:
            result = result + rec_guess
        else:
            result = result + cur_dash[i]
    return result

words = ["bob","cool", "whatup"]

secret_word = random.choice(words)
get_guess()