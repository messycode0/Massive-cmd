import os
import random
import time


# a funcion to clear the console
clear = lambda: os.system('cls')

# counts the plays
timesUsrPlayed = 0

def randomPartOfGame():    
    global timesUsrPlayed
    n = random.randint(0,60)
    p = random.randint(0,60)
    print(f"{n} and {p}")

    if n != p:
        print("im sorry try again")
        timesUsrPlayed += 1
        randomPartOfGame()
        
    elif n == p:
        timesUsrPlayed += 1
        print(f"yay you did, it took you {timesUsrPlayed} times to get a double")
        timesUsrPlayed = 0
    


def mainGameFunction():
    print('game starting...')
    time.sleep(2)
    clear()
    print('welcome you need to get a double in dice (is means get the same number)')
    randomPartOfGame()