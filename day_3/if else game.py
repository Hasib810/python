print("welcome to temple run")
choice1 = input("you are in cross road. where do you want to go? left or right: ").lower()
if choice1 == "right":
    print("youre in danger zone, game over.")
else:
    print("you are in safe zone, you can move forward.")
choice2 = input("you are in a middle of a river, do you want to swim or wait for a boat?: ").lower()
if choice2 == "swim":
    print("you are eaten by a crocodile, game over.")
else:
    print("you are safe now, you cane move forward.")
    choice3 = input("there are 3 doors, red yellow and green, choose one: ").lower()
    if choice3 == "red":
        print("you are burned by fire, game over.")
    elif choice3 == "yellow":
        print("you are eaten by a beast, game over.")
    else:
        print("you win, you found the treasure.")


