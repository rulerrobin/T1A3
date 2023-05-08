class MyClass:
    def my_func(self):
        print("Hello, world!")

class player():
    def __init__(self, weapon):
    # initialize player
    # set weapon to false
        self.weapon = False


class rooms(): 
    # Starting room 
    # 1. Describe the room to player

    def monsterRoom():
        print ("As you enter the room you hear a grunt and eyes staring into your soul.\n ITS A MONSTER!" )

        fight_flee = input("Do you 'fight' or 'flee'?\n")
        if (fight_flee == 'fight' and player.weapon() == False):
            print ("YOU HAVE DIED")
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