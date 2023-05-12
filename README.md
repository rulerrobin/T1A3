# Basic RPG Adventure!
***
## Repo Link
***

[Github Link](https://github.com/rulerrobin/T1A3)
## Summary of Features and coding styles
***

**The Basic RPG adventure** is a command line application that was planned and developed in about 1 week for the Coder Academy Term 1 Assessment 3 in the Accelarated 2023 March Cohort. This application was used to test our skills in project management and development within a short time period. The coding style guide that was being followed is the [pep8](https://peps.python.org/pep-0000/) guide which I have attempted to adhere to as well as fix code later on to follow it. 

### **Features**

The features of the RPG adventure game are as follows:

**User Input**
The user will be able to input their name into the game at the start and it will be used as part of the intro question if they wish to play the game. 

Through user input once the game is accepted the user will be able to move around the rooms using selected parameters given to the player, these parameters are validated to make sure that they are valid using a while loop to check if they have made a valid choice as of yet and if so to call another function to activate the next room. 

**Weapon Check**
Allow user to pick up a weapon and in a room and if the player tries to pick it up again the weapon is no longer available printing out new text that instead says the weapon is no longer where it was. The player will now have set the weapon to `True` which is then referenced by the code in a specific room of the game. This room checks if player has the weapon or not and depending on their choice to fight or flee they will either escape or die.

**Random Number**
The game has a puzzle that generates a random number each time it is run and printed out to a CSV file. This file containing the number can be read by the player once they interact with the specific area required. This number can then be used to escape the dungeon by inputting it into another area of the maze and let the player through. The player only has 3 guesses otherwise they will die. However if the player decides to leave the guessing game, the number of guesses will reset back to 0.

**Validation**
In each of the options of code within the game there is validation code that protects the player from having a runtime error and tells them to input the valid parameters needed to get through./

## Deevelopment Plan

I used Notion for my project tracker, the reason for this is because I use Notion to track all of the other projects I am working on and I have gotten used to using it. However it does have less functionality for a kanban board as it only has To-do, In progress and Done functionality for the board. However it does have more options when changed to different formats such as table format.

[Notion Board](https://www.notion.so/04cbbf4830ca45d7a465c5e1428629fa?v=1d9767f49a244dc59d32a73a2047e533&pvs=4)

The development plan that I made was heavily focused on planning. I used a kanban style board to build a project management system that allowed to me complete tasks day to day as well as move them/change them if needed.

**Priorities**
The priority features of the game to make it an MVP were as follows:
1. Make each room and and their navigation options first as I'm planning each to have their own method
2. Make the death / quit room method since it's simple enough to do
3. The fight room without weapon since can add on later
4. The quiz room & library / clue room to do export