from sys import exit
import random
import time
min = 1
max = 6
player = input("Enter your name: ")
computer = ["alpha", "beta", "gamma", "neuro", "vision","grapho"]
for name in random.sample(computer,1):
    computer = name
again = "yes"
while again == "yes":
    if again == "no":
        exit(0)
    time.sleep(1)
    print(" Your turn \n")
    time.sleep(1)
    print(" Dice is rolling \n ")
    time.sleep(2)
    x =random.randint(min,max)
    y =random.randint(min,max)
    def dice(d):
        if d ==1:
            print('''
            --------------
            |             |
            |             |
            |      *      |
            |             |
            ---------------
            ''')
        elif d == 2:
            print('''
            ----------------
            |              |
            |       *      |
            |              |
            |       *      |
            ----------------
           ''' )
        elif d== 3:
            print('''
            ----------------
            |              |
            |       *      |
            |       *      |
            |       *      |
            ----------------
            ''')
        elif d == 4:
            print('''
            ----------------
            |              |
            |   *      *   |
            |              |
            |   *      *   |
            ----------------
                ''')
        elif d== 5:
            print('''
            ----------------
            |              |
            |   *      *   |
            |      *       |
            |   *      *   |
            ----------------
                ''')
        elif d==6:
            print('''
            ----------------
            |              |
            |   *      *   |
            |   *      *   |
            |   *      *   |
            ----------------
                ''')
    dice(x)
    time.sleep(1)
    print("\n")
    print(str(computer)+"'s turn")
    time.sleep(1)
    print("\n Dic is  rolling..")
    time.sleep(2)
    dice(y)
    time.sleep(1)
    if x == y:
        print("\n It's draw.")
        time.sleep(1)
        print("\n Input yes to play again or no to exit")
    elif x > y:
        print("\n You won, Congrats \n")
        time.sleep(1)
        print("\n Input yes to play again or no to exit")
    elif x < y:
        print("\n Sorry, you lost. Try again")
        time.sleep(1)
        print("\n Input yes to play again or no to exit")
    again = input(str(player)+ "  would u like to roll the dice again?")