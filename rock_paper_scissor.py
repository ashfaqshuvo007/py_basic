from random import randint

#create an array of all the options
options = ["Rock", "Paper", "Scissors"]

#set computer to select any option
Computer = options[randint(0,2)]

#set player to false
player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    
    if player == Computer:
        print("Computer: {}".format(Computer))
        print("Player: {}".format(player))
        print("Tie!")
        
    elif player == "Rock":
        if Computer == "Paper":
            print("Computer: {}".format(Computer))
            print("Player: {}".format(player))
            print("Ooops! You loose!")
        else:
            print("Computer: {}".format(Computer))
            print("Player: {}".format(player))
            print("Great! You win!")
            
    elif player == "Paper":
        if Computer == "Scissors":
            print("Computer: {}".format(Computer))
            print("Player: {}".format(player))
            print("Ooops! You loose!")
        else:
            print("Computer: {}".format(Computer))
            print("Player: {}".format(player))
            print("Great! You win!")
            
    elif player == "Scissors":
        if Computer == "Rock":
            print("Computer: {}".format(Computer))
            print("Player: {}".format(player))
            print("Ooops! You loose!")
        else:
            print("Computer: {}".format(Computer))
            print("Player: {}".format(player))
            print("Great! You win!")
    else:
        print("Computer: {}".format(Computer))
        print("Player: {}".format(player))
        print("That's not a valid option! Check your spelling")
    player = False
    Computer = options[randint(0,2)]             
    
    

