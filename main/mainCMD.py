from time import time
import videoGamefRichieCMD
import os, time

clear = lambda: os.system('cls')

print("loading...")
time.sleep(0.5)
clear()

print("welcome to richie CMD")

def mainCMD():

    command = input('>')

    if command == 'help':
        print('video game = videoGame or vg')
        print('exit Program = close or exit')
        print('clear the console = clear or cls')
    
    if command == 'clear' or command == 'cls':
        clear()

    if command == 'close' or command == 'exit':
        print(0/0)

    if command == 'vg' or command == 'videoGame':
        videoGamefRichieCMD.mainGameFunction()




    mainCMD()
mainCMD()