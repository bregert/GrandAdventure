from random import choice

name = input("Hey type your name: ")
print("Hello " + name + " Welcome to Adventure Sands")

should_we_play = input(("Would you like to go on an adventure? ").lower())


if should_we_play == "y" or should_we_play == "yes":
    print("The Great Adventure Awaits!")
    weapon = input("Choose a weapon, Axe or Sword!: ").lower()

    direction = input("Do you want to go right or left?: ").lower()
    if direction == "right":
        choice == input("You see a mage, do you battle, yes or no?: ").lower()
        if choice == "yes":
            print("You fought bravely, however you died in combat")
        else:
            print("You Won the Grand Adventure!")
    else:
        print("You went left, got lost, and died from starvation...sad")

else:
    print("I guess I will continue my search for a REAL Hero")
