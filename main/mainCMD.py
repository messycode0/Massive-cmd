from time import time
import videoGamefRichieCMD
import os, time

clear = lambda: os.system('cls')

#loads all things
print("loading...")
time.sleep(0.5)
clear()

print("welcome to richie CMD")

#main function
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



    #calls the function again to have multible commads
    mainCMD()
#calls the function when its starts
mainCMD()
