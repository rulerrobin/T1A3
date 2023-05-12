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

            while True: # loop until a valid choice is made
                pick_up = input("Do you pick up the weapon? (y/n)\n")
                if pick_up.lower() == 'y':
                    self.player.get_weapon()
                    print("You pick up the weapon and now have a weapon and return to the previous location")
                    self.skeletalRoom()
                elif pick_up.lower() == 'n':
                    print("You decide to leave the hilt and go back to the previous location")
                    self.skeletalRoom()
                    break
                else:
                    print ("Invalid input please use 'y' or 'n'")    
        else: # if player weapon is True
            print("You see the hole where the blade used to be. Other than that, it's just a dead end wall. You return to the previous room.")
            self.skeletalRoom()
    
    def skeletalRoom(self):
        allowed_choices = ['forward', 'left', 'back'] #list of possible choices
        while True:
            choice = input("You are in a room filled with skeletons do you go 'forward' or 'left' or 'back'? \n")
            if choice.lower() in allowed_choices:
                break
            print("Invalid input, please use a valid option")

        # once a valid choice is made
        if choice.lower() == 'forward':
            print("The door ahead opens into a dead end wall and go back to the previous room")
            self.skeletalRoom()
        elif choice.lower() == 'left':
            self.weaponRoom()
        elif choice.lower() == 'back':
            self.createRoom()

    def monsterRoom(self):
        print("As you enter the room you hear a grunt and eyes staring into your soul. ITS A MONSTER!")
        while True:
            fight_flee = input("Do you 'fight' or 'flee'?\n")
            if fight_flee == 'fight' and not self.player.weapon:
                print("YOU HAVE NO WEAPON AND DIED")
                quit() # on death quit
            elif fight_flee == 'flee' and not self.player.weapon:
                print ("You escape the room and return to the previous location")
                self.scaryRoom()
            elif fight_flee == 'fight' and self.player.weapon:
                print("YOU HAVE ESCAPED")
                return
            elif fight_flee == 'flee' and self.player.weapon:
                print ("You escape the room and return to the previous location")
                self.scaryRoom()
            else:
                print ("Please enter a valid input")


    # Forward from Main Room
    def scaryRoom(self):
        while True:
            choice = input ("You are in scary room go 'right' 'left' or 'back'?\n ")
            if choice == 'right':
                self.monsterRoom()
            elif choice == 'left': # Instant Death
                print("As you walk into the room you hear crumbling and all of a sudden the floor collapses. You have died")
                return
            elif choice == 'back':
                print ("You return to the starting room")
            else:
                print ("Please enter a valid input")

    # Puzzle Room

    def puzzleRoom(self):
        while True:
            choice = input("You are in a room filled with what seems to be images and some doors. Do you go 'forward' 'back' or 'right'?\n")
            if choice == "forward":
                self.puzzleClue()
            elif choice == 'back':
                self.createRoom()
            elif choice == 'right':
                self.puzzleEscape()
            else: 
                print ("Please enter a valid input")


    def puzzleEscape(self):
        attempts = 0
        guessing = True

        while guessing:

            print ("As you look closer at the door and you try to fill in a 8 digit code)")
            user_input = input ("Enter an 8 digit number \n")
            if len(user_input) == 8 and user_input.isdigit():
                # Check if player is correct
                if user_input == random_number:
                    print('As soon as you enter the numbers doors begin to move and you escape the dungeon!')

                else:
                    again = input('Sorry, your guess is incorrect. Try again? (y/n)\n')
                    if again.lower() == "n":
                        print ('You hear something above you turning as you return to the center of the room')
                        guessing = False
                        self.puzzleRoom()
                    elif again.lower() == "y":
                        attempts += 1
                        print(f"You have {3-attempts} attempts left.")

                        if attempts == 3:
                            break
                        else:
                            # reset guessing to True and prompt for input again
                            guessing = True
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")   
            else:
                print("Invalid input. Please enter an 8-digit number")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

        print ("The ceiling suddenly opens up and a spike trap comes hurtling down killing you.")
        quit() # on death quit



    def puzzleClue(self):
        choice = input('You see a book that looks like it relates to the door on the right. Read it? (y/n)\n')
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
    def createRoom(self, instance):
        while True:
            choice = input("You are in a room filled with torches with a few choices of direction. Do you go 'forward' 'back' 'left' or 'right'?\n")
            if choice == "forward":
                self.scaryRoom()
            elif choice == 'back':
                print("You attempt to use the back door of the room but it opens into a dead end")
            elif choice == 'right':
                self.skeletalRoom()
            elif choice == 'left':
                self.puzzleRoom()
            else:
                print ("Please enter a valid input")
