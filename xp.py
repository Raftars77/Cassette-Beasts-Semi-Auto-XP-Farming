import pyautogui
import time
import os
import winsound

FREQ=1000 #Sound frequency
DUR=500 #Duration in ms

#Shift for running
def shift():
    for _ in range(0,2):
        time.sleep(1.5)
        print("Shift-down")
        pyautogui.keyDown('shift')
        time.sleep(1)
        pyautogui.keyUp('shift')
        print("Shift-up")

#Boss stage
def boss():
    #Check if boss is oneshoted or it failed
    location1,location2,location3 = None,None,None
    while location1 is None and location2 is None:
        print("No results")
        location1 = pyautogui.locateOnScreen('img2.png',confidence=0.6)
        if location1 is not None:
            print("Boss not killed")
            winsound.Beep(FREQ,DUR)
            exit(1)
        location2 = pyautogui.locateOnScreen('img3.png',confidence=0.6)
        time.sleep(1)
    
    #Check if any tape has lvl up to 5 stars
    print("Battle finished")
    location3 = pyautogui.locateOnScreen('img4.png',confidence=0.9)
    if location3 is not None:
        print("Lvl up")
        winsound.PlaySound('lvl.wav',winsound.SND_FILENAME)
        return True
    pyautogui.keyDown('tab')
    time.sleep(0.2)
    pyautogui.keyUp('tab')
    print("Tab")
    time.sleep(2)
    return False


def main():

    os.system('pause')
    time.sleep(8)

    while True:

        #Stage from entrance to boss room
        pyautogui.keyDown('w')
        print("W-down")
        shift()
        pyautogui.keyDown('space')
        print("Space-down")
        time.sleep(1)
        pyautogui.keyUp('space')
        pyautogui.keyUp('w')
        print("W-up\nSpace-up")
        
        #Boss stage
        if boss() is True: 
            os.system('pause')
            time.sleep(8)
            continue

        #Stage from boss room to entrance
        pyautogui.keyDown('s')
        pyautogui.keyDown('space')
        print("S-down")
        print("Space-down")
        time.sleep(1)
        pyautogui.keyUp('space')
        shift()
        pyautogui.keyUp('s')
        print("S-up\nSpace-up")

        time.sleep(2)


main()