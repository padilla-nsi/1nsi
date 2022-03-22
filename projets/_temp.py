import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

from time import sleep

delta = 0.2

for i in range(10):
    print("ABCDE")
    print("OOOOO")
    clear()
    print("ABCDE")
    print("OOOOO")
    sleep(delta)
    clear()
    print("ABCDE")
    print("XOOOO")
    sleep(delta)
    clear()
    print("ABCDE")
    print("OXOOO")
    sleep(delta)
    clear()
    print("ABCDE")
    print("OOXOO")
    sleep(delta)
    clear()
    print("ABCDE")
    print("OOOXO")
    sleep(delta)
    clear()
    print("ABCDE")
    print("OOOOX")
    sleep(delta)
    clear()
    print("ABCDE")
    print("OOOOO")
    clear()