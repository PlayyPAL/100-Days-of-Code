print(r'''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ : : : : : : : : : : : : : : : @
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 |                             |
 |  \|/        %%%        \|/  |
 |  -t-     %%%%%%%%%     -t-  |
 |  /|\     \  %%%  /     /|\  |
 |         \ / %%% \ /         |
 \        - |  %%%  | -        /
  \       - |  %%%  | -       /
   \       / \     / \       /
    \        / --- \        /
     \         ! !         /
      \ __ ___ __ ___ ___ /
      ( ___ ___ __ _ ___  )
       (88888888888888888)
        --\ --------- /--
          ((((((o))))))
           \         /
            | | | | |
            | | | | |
            | | | | |
            | | | | |
            | | | | |
            | | | | |
            | | | | |
            | | | | |
          _(IIIIIIIII)_
       __/_____________\__
  ____/___________________\____
 /_____________________________\
(_______________________________)
''')
print("Welcome to the Grail Trail.")
print("Your mission is to trek the trail to find the...")
print('''
                                  88 88  
                                  "" 88  
                                     88  
 ,adPPYb,d8 8b,dPPYba, ,adPPYYba, 88 88  
a8"    `Y88 88P'   "Y8 ""     `Y8 88 88  
8b       88 88         ,adPPPPP88 88 88  
"8a,   ,d88 88         88,    ,88 88 88  
 `"YbbdP"Y8 88         `"8bbdP"Y8 88 88  
 aa,    ,88                              
  "Y8bbdP"                               
''')

# Beginning
left_right = input('The trail begins in an empty forest. '
                   'You\'re senses become heightened. '
                   'You come to a crossroad, where do you want to go? "left" or "right"\n ')
if left_right.lower() == "left":
    print("Ooooohh...a meteor landed on you. Tough break.")
elif left_right.lower() == "right":
    jeep_shack = input(
        'You find a shack with a jeep parked outside. Do you "drive" or "go in"?\n ')
    if jeep_shack.lower() == "drive":
        print("BOOOOOMMM! The jeep exploded when turning the ignition. "
              "Your funeral had a nice turnout though.")
    elif jeep_shack.lower() == "go in":
        doors = input('Once inside, you go down a hallway. '
                      'At the end of the hall, you reach 3 doors. '
                      'Choose 1? "Brown", "White", or "Blue"\n ')
        if doors.lower() == "white":
            print("You chose..... Poorlyy. "
                  "You've entered a yeti's lair while he is enjoying dinner."
                  " You became a scrumptious dessert.")
        elif doors.lower() == "brown":
            print("You chose...... Poorlyy. The ground is an illusion and you fell to an empty void and "
                  "float through time and space to a prolonged agony of pain and horror. Game Over. ")
        elif doors.lower() == "blue":
            print("You chose...... Wisely! You found the GRAIL!! ")
        else:
            print("No. Not cool..")
    else:
        print("Bingo bongo wrongo... try again..")
else:
    print("That's against the rules. Tisk tisk..")
