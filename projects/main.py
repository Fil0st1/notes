import random


computer = random.choice([0, 1, 2])
gameDict = {    
    "Snake": 0,
    "Water": 1,
    "Gun": 2,
}

print("Thanks for playing this game! \n\n To play this game choose any 1 option from these: \n s: Snake\n w: Water \n g: Gun")
Your_Choice = input("Enter your choice: ")
Your_Dict = {
    "s": 0,
    "w": 1,
    "g": 2,
}

a = Your_Dict[Your_Choice]
# print(a)
# print(computer)
 
if ( computer == a):
    print("We both chose same choice")
else:

    if (computer == 0 and a == 1):
        print("Computer chose: Snake \nYou chose: Water \nYou Lost!!")
    elif (computer == 0 and a == 2):
        print("Computer chose: Snake \nYou chose: Gun \nYou Won!!")

    elif (computer == 1 and a == 0):
        print("Computer chose: Water \nYou chose: Snake \nYou Won!!")
    elif (computer == 1 and a == 2):
        print("Computer chose: Water \nYou chose: Gun \nYou Lost!!")

    elif (computer == 2 and a == 0):
        print("Computer chose: Gun \nYou chose: Snake \nYou Lost!!")
    elif (computer == 2 and a == 1):
        print("Computer chose: Gun \nYou chose: Water \nYou Won!!")
    else:
        print("Something went wrong!!")