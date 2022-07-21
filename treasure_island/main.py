print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
to_go = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n')
if to_go == "left":
    action = 'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
    if action == "wait":
        doors = input("You arrive on the island safe and sound. There is a house with 3 doors. One red, one yellow and one blue. What color will you choose?")
        if doors == "red":
            print("This is a room full of fire. The game is over.")
        elif doors == "yellow":
            print("You found a treasure! You have won!")
        elif doors == "blue":
            print("You enter the room with the beasts. The game is over.")
        else:
            print("You have chosen a non-existent door. The game is over.")
    else:
        print("You were attacked by an angry trout. The game is over.")
else:
    print("You fell into a hole. Game Over.")