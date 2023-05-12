from rooms import rooms, player
from art import *
from colorama import Fore, Back

# Create instance of it
gaming = rooms()
# Main
art = text2art("T  1  A  3")
print (art) # prints out T1A3 as ascii art
print (Fore.RED) #change tex to tred
print (Back.GREEN) # change background color to green
# 1. When player opens game welcome to the game
# 2. Ask player for their name
# 3. Ask player using name if they want to play
# 4. If yes change game to True 

while True:
    PLAYER_NAME = input("Welcome to the game! Please enter your name: ")
    while PLAYER_NAME.strip() != "":
            # strip clearing end and start white space
            game_state = input(f'{PLAYER_NAME.strip()}, would you like to play? (y/n):\n')
            if game_state == 'y':
                    gaming.createRoom(gaming)
            elif game_state == 'n':
                print ("Game will now quit.")
                quit()
            else:
                print ("Invalid input please use 'y' or 'n'")
    else: 
        print ("Invalid input please do not leave blank")
            

    # 4.1. Start loop
        # 4.1.a.If player dies ask to play again
        # 4.1.b If player escapes ask to play again
            # if player says no then quit game
# . If not set game to False and quit the application
# print (f'{PLAYER_NAME}, thank you for playing!')
