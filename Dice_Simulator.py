#dice roll Simulator app

import random
import time


print("      --------------------------------------------------------------------------------------------------------   ")
print("     |         _________              _________   _________                       _________                   |  ")
print("     |        |           |        | |         | |           \     /     /\      |           |        |       |  ")
print("     |        |           |        | |         | |            \   /     /  \     |           |        |       |  ") 
print("     |        |_________  |________| |_________| |_______      \ /     /    \    |_________  |________|       |  ")
print("     |                  | |        | | \         |              |     /------\             | |        |       |  ")
print("     |                  | |        | |    \      |              |    /        \            | |        |       |  ")
print("     |         _________| |        | |       \   |_________     |   /          \  _________| |        |       |  ")
print("     |                                                                                                        |  ")
print("      --------------------------------------------------------------------------------------------------------   ")
print()
print()
print()
print()
print("               Dice Rolling by Shreyash...                                                            ")


time.sleep(5)


x = "y"

while (x == "y") :
    
    print()
    print()
    number = random.randint(1,6)

    if number == 1:
        print("       _____________")
        print("      |             |")
        print("      |             |")
        print("      |      O      |")
        print("      |             |")
        print("      |_____________|")
        print()
        

        
    if number == 2:
        print("       ____________")
        print("      |            |")
        print("      |   O        |")
        print("      |            |")
        print("      |       O    |")
        print("      |____________|")
        print()
        


        
    if number == 3:
        print("       ____________")
        print("      |            |")
        print("      |  O         |")
        print("      |     O      |")
        print("      |         O  |")
        print("      |____________|")
        print()
        


        
    if number == 4:
        print("       ____________")
        print("      |            |")
        print("      | O       O  |")
        print("      |            |")
        print("      | O       O  |")
        print("      |____________|")
        print()
        


        
    if number == 5:
        print("       ____________")
        print("      |            |")
        print("      |  O      O  |")
        print("      |     O      |")
        print("      |  O      O  |")
        print("      |____________|")
        print()
        


        
    if number == 6:
        print("       ____________")
        print("      |            |")
        print("      |  O      O  |")
        print("      |  O      O  |")
        print("      |  O      O  |")
        print("      |____________|")
        print()
        
    
    print()
    print()

    x = input("      Press 'y' if you want to roll again:  ")