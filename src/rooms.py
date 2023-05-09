class player():
    def __init__(self, weapon):
        self.weapon = False # initiates weapon and sets to False


    def get_weapon(self):
        self.weapon = True # sets weapon to True when called

class rooms(): 

    def weaponRoom():
        # makes a player instance without a weapon
        weapon = player()

        if not weapon.weapon:
            print ("You see the hilt of a blade lodged into a wall")

            pick_up = input("Do you pick up the weapon? (y/n): ")
            if pick_up == 'pick up':
                weapon.get_weapon()
                print("You pick up the weapon and now have a weapon!")
            skeletalRoom()
        elif not weapon.weapon():
            print ("It's just a dead end wall")
            skeletalRoom()
    
    def skeletalRoom():
        print
        pass

    def monsterRoom():
        weapon = player(weapon)
        print ("As you enter the room you hear a grunt and eyes staring into your soul.\n ITS A MONSTER!" )
        weapon 
        fight_flee = input("Do you 'fight' or 'flee'?\n")
        if (fight_flee == 'fight' and not weapon.weapon):
            print ("YOU HAVE NO WEAPON AND DIED")
            quit()
        elif (fight_flee == 'fight' and  weapon.weapon):
            print ("YOU HAVE ESCAPED")
            quit()


    def scaryRoom():
        print("You are in scary room go 'right' or 'left'\n")
        choice = input ("")
        if choice == 'right':
            rooms.monsterRoom()
        if choice == 'left': # Instant Death
            print ("As you walk into the room you hear crumbling and all of a sudden the floor collapses.\n You have died")
            quit() # Needs to go back to loop to the welcome perhaps a boolean return?


    def createRoom(self):
        choice = input ("You are in a room filled with torches with a few choices of direction.\n Do you go 'forward' 'back' 'left' or 'right'?\n")
        if choice == "forward":
            rooms.scaryRoom()
        elif choice == "back":
            print ("You attempt to use the back door of the room but it opens into a dead end")

    # 2. Ask player to decide which direction to go
    # 3. Depending on choice move to the room (right or forward)

class exitRoom():
    # Basic room to exit from the dungeon probably boolean return for quit

    pass


class ghostRoom():
    #n Next to a death room, scary text and exit opposite
    pass



class Fight():
    pass

# Extras