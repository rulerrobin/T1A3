import csv
import random

# Global available variable since its just for reading through csv files
random_number = str(random.randint(10000000, 99999999))
# write to file 
with open('random_number.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([random_number])

class player():
    def __init__(self, weapon=False):
        # initiates weapon and sets to False
        self.weapon = weapon

    def get_weapon(self):
        self.weapon = True # sets weapon to True when called


class rooms:
    def __init__(self):
        # creates usable instance of player for weapon
        self.player = player()

    # Right side of the main room
    def weaponRoom(self):
        # check if player weapon = True
        if not self.player.weapon:
            print("You see the hilt of a blade lodged into a wall")
            pick_up = input("Do you pick up the weapon? (y/n): ")
            if pick_up == 'y':
                self.player.get_weapon()
                print("You pick up the weapon and now have a weapon!")
                self.skeletalRoom()
            else:
                print("No")
        else:
            print("You see the hole where the blade used to be. Other than that, it's just a dead end wall")
            self.skeletalRoom()
    
    def skeletalRoom(self):
        choice = input ("Skeletal Room can choose 'forward' or 'left' or 'back': ")

        if choice == 'forward':
            print ("The door ahead opens into a dead end wall and go back to the previous room")
            self.skeletalRoom()
        elif choice == 'left':
            self.weaponRoom()
        elif choice == 'back':
            self.createRoom()

    def monsterRoom(self):
        print("As you enter the room you hear a grunt and eyes staring into your soul. ITS A MONSTER!")
        fight_flee = input("Do you 'fight' or 'flee'?: ")
        if fight_flee == 'fight' and not self.player.weapon:
            print("YOU HAVE NO WEAPON AND DIED")
            quit()
        elif fight_flee == 'fight' and self.player.weapon:
            print("YOU HAVE ESCAPED")
            quit()

    # Forward from Main Room
    def scaryRoom(self):
        print("You are in scary room go 'right' or 'left': ")
        choice = input ("")
        if choice == 'right':
            self.monsterRoom()
        if choice == 'left': # Instant Death
            print("As you walk into the room you hear crumbling and all of a sudden the floor collapses. You have died")
            quit() # Needs to go back to loop to the welcome perhaps a boolean return?

    # Puzzle Room

    def puzzleRoom(self):
        choice = input("You are in a room filled with what seems to be images and some doors. Do you go 'forward' 'back' or 'right'?: ")
        if choice == "forward":
            self.puzzleClue()
        elif choice == 'back':
            self.createRoom()
        elif choice == 'right':
            self.puzzleEscape()


    def puzzleEscape(self):
        attempts = 0
        guessing = True

        while guessing:

            user_input = input ("As you look closer at the door there is a puzzle requiring a series of numbers to be entered. ")

            # check if input is a 8 digit number
            if len(user_input) == 8 and user_input.isdigit():
                # Check if player is correct
                if user_input == random_number:
                    print('As soon as you enter the numbers doors begin to move and you escape the dungeon!')
                    print ('End') # debug
                    return

                else:
                    again = input('Sorry, your guess is incorrect. Try again? (y/n): ')
                    if again.lower() == "n":
                        print ('You hear something above you turning as you return to the center of the room')
                        guessing = False
                        self.puzzleRoom()
                    elif again.lower() == "y":
                        attempts += 1
                        print(f"You have {3-attempts} attempts left.")

                        if attempts == 2:
                            break
                        else:
                            # reset guessing to True and prompt for input again
                            guessing = True
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                    
            else:
                print('Invalid input. Please enter an 8-digit number or an interactable command.\n')

        print ("The ceiling suddenly opens up and a spike trap comes hurtling down killing you.")


    def puzzleClue(self):
        choice = input('You see a book that looks like it relates to the door on the right. Read it? (y/n): ')
        if choice == 'y':
        # Read the random number from the CSV file and provide the first digit as a clue
            with open('random_number.csv', mode='r') as file:
                reader = csv.reader(file)
                random_number = next(reader)[0]
            print(f'A series of numbers is written over and over again, the number is: {random_number} you return to the center of the room.' )
            self.puzzleRoom()
        else:
            print('You return to the center of the room')

    # MAIN ROOM 
    def createRoom(self):
        choice = input("You are in a room filled with torches with a few choices of direction. Do you go 'forward' 'back' 'left' or 'right'?: ")
        if choice == "forward":
            self.scaryRoom()
        elif choice == 'back':
            print("You attempt to use the back door of the room but it opens into a dead end")
        elif choice == 'right':
            self.skeletalRoom()
        elif choice == 'left':
            self.puzzleRoom()
