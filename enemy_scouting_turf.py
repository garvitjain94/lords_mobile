"""
enemy_scouting_turf.py
- script will keep monitoring the screen for "An enemy is scouting your Turf/Camp". 
- If string is present, it will start making sound. Please keep speaker volume audible.
 
Inputs:
    None

- Runs continuously | Press Ctrl+Z in terminal to stop/reset.
"""
import sys
import time

import pyautogui
import pytesseract

# this is to have time to bring the game window on the top/front
print("Waiting 5 sec")
time.sleep(5)

while(1):
    # runs every 1 sec
    time.sleep(1)
    # screen coordinates of the message that appear on the game window
    pyautogui.screenshot("enemy_scouting_turf.png",
                         region=(580*2, 420*2, 1000, 80))
    price_string = pytesseract.image_to_string(
        'enemy_scouting_turf.png').split()

    # if an enemy starts scouting your turf/camp, the script generates 10 beeps
    if "scouting" in price_string:
        ctr = 10
        while(ctr):
            print("\a")
            ctr -= 1
            time.sleep(0.5)
