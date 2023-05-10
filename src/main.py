from rooms import rooms
from rooms import player


# Create instance of it

game = rooms()

# Main

# 1. When player opens game welcome to the game
# 2. Ask player for their name
PLAYER_NAME = input("Welcome to the game! Please enter your name: ")
# 3. Ask player using name if they want to play
game_state = input(f'{PLAYER_NAME} would you like to play? (y/n)\n')
# 4. If yes change game to True 
if game_state == 'y':
    while True:
        game.createRoom()
    

    # 4.1. Start loop
        # 4.1.a.If player dies ask to play again
        # 4.1.b If player escapes ask to play again
            # if player says no then quit game
# . If not set game to False and quit the application
# print (f'{PLAYER_NAME}, thank you for playing!')
