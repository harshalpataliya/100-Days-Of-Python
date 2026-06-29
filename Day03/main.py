print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input('you\'re at a cross road .where do you want to go?\n '
             'Type "left" or "right" to go left"\n').lower()

if choice1=="left":
    choice2=input('You\'ve came to the lake.'
                'There is an island in the middle of lake.\n'
                'Type "wait" for a boat.'
                'Type "swim" to swim across.\n').lower()
    if choice2=="wait":
        choice3=input('You arrive at the island.\n'
                      'There is a House in the middle of island with Three Doors.\n'
                      'One is red, One is yellow, and One is blue.\n'
                      'Which Color do you choose?..').lower()

        if choice3=="red":
            print("You enter the room of snakes.Game Over!")
        elif choice3=="yellow":
            print("You found the Lost Hidden treasure.You Win!")
        elif choice3=="blue":
            print("You enter the room of Beasts.Game Over!")
        else:
            print("You enter the room that doesn't exist.And You found the hidden room in game.  ")
    else:
        print("You attack by Crocodile.Game Over!")
else:
    print('You fall into a hole \n'
          'Game Over!')