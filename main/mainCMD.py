from time import time
import jaketools
import videoGamefRichieCMD
import WYR
import os, time



#loads all things
print("loading...")
jaketools.wait(2)
jaketools.clear()

print("welcome to MASSIVE CMD")

#main function
def mainCMD():

    command = input('>>>')

    if command == 'help':
        print('video game = videoGame or vg')
        print('exit Program = close or exit')
        print('clear the console = clear or cls')
        print('would you rather = wyr or would you rather')
    
    if command == 'clear' or command == 'cls':
        jaketools.clear()

    if command == 'close' or command == 'exit':
        print(0/0)

    if command == 'vg' or command == 'videoGame':
        videoGamefRichieCMD.mainGameFunction()

    if command == 'wyr' or command == 'would you rather':
        WYR.mainFunction()



    #calls the function again to have multible commads
    mainCMD()
#calls the function when its starts
mainCMD()
