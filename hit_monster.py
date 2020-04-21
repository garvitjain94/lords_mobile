"""
hit_monster.py

Inputs:
    Screen coordinates of the monster i.e. screen coordinates of the center of the bluestacks window | Screen coordinates can be found by Shift+Command+4
    Repeat interval = (Time to travel to monster * 2) + 10 | +10 to take into account time spent at monster and safe buffer time
"""
import pyautogui
import time

# this is to have time to bring the game window on the top/front
print("Waiting 5 sec")
time.sleep(5)

# number of times you wish/know to hit the monster
number_of_hits = 3

while(number_of_hits):
    # monster coordinates (not turf coordinates, screen coordinates)
    # IMPORTANT : For first time, once your heroes start and reach the monster, record the screen coordinates.
    #     On mac, press Shift+Command+4 to get the crosshair. Take it to the monster position.
    # Fo my mac, x=850, y=525 are the screen coordinates
    # For subsequent runs, scroll in the game to bring your monster to above screen coordinates before starting the script.
    pyautogui.moveTo(850, 525)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # screen coordinates for 1 hit
    # Fo my mac, x=930, y=630 are the screen coordinates
    # These coordinates once configured, won't change
    pyautogui.moveTo(930, 630)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # screen coordinates for sending heroes | Assuming you dont want to change heroes
    # Fo my mac, x=1212, y=730 are the screen coordinates
    # These coordinates once configured, won't change
    pyautogui.moveTo(1212, 730)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(30)
    number_of_hits -= 1
