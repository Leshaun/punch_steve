from function import punch
from list import steve

while steve.hitpoints > 0:
    action_taken = input("Would you like to punch " + steve.name + "?\n y/n")
    if action_taken == "y":
        steve.hitpoints = steve.hitpoints - punch()
        print(steve.name + " has " + str(steve.hitpoints) + " hitpoints remaining.")
    elif action_taken == "n":
        print("You chose not to punch " + steve.name + " this time.")
    else:
        print("Please enter y/n")