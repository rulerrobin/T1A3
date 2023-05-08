class player():
    def __init__(self, weapon):
        self.weapon = weapon # initiates there is a weapon option

    def get_weapon(self):
        self.weapon = True # sets weapon to true when called

class rooms(): 
    def weaponRoom():
        weapon = player(False)
        print ("You see the hilt of a blade lodged into a wall and try to pull it out.\n")

        pick_up = input("Do you pick up the weapon? (y/n): ")
        if pick_up == 'pick up':
            weapon.get_weapon()
            print("You pick up the weapon and now have a weapon!")

    def monsterRoom():
        weapon = player(weapon)
        print ("As you enter the room you hear a grunt and eyes staring into your soul.\n ITS A MONSTER!" )
        weapon 
        fight_flee = input("Do you 'fight' or 'flee'?\n")
        if (fight_flee == 'fight' and  weapon.weapon == False):
            print ("YOU HAVE DIED")
            quit()
        elif (fight_flee == 'fight' and  weapon.weapon == True):
            print ("YOU HAVE ESCAPED")
            quit()


    def scaryRoom():
        print("You find within this room there are skeletons strewn about the floor. You have the option to go either 'left or right'\n")
        choice = input ("")
        if choice == 'right':
            rooms.monsterRoom()


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

class skeletalRoom():

    pass

class ghostRoom():
    #n Next to a death room, scary text and exit opposite
    pass



class Fight():
    pass

# Extras