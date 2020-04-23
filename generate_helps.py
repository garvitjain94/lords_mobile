"""
generate_helps.py

Inputs:
    Screen coordinates of the farm

NOTE : 
- For sending helps, I upgrade farm (because it doesn't require food, also not available on turfs with high no of troops/upkeep). 
- This script puts farm to upgrade, click for help and cancels the upgrade within 2 seconds.
- Runs continuously | Press Ctrl+Z in terminal once target helps achieved.
"""
import pyautogui
import time

# this is to have time to bring the game window on the top/front
print("Waiting 5 sec")
time.sleep(5)

while(1):
    # screen coordinates of farm
    pyautogui.moveTo(850, 525)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # screen coordinates for "Upgrade" button
    pyautogui.moveTo(1200, 850)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # screen coordinates for "Upgrade" button
    pyautogui.moveTo(1200, 850)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # screen coordinates of farm
    pyautogui.moveTo(850, 525)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # screen coordinates for "Help" button
    pyautogui.moveTo(1200, 850)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(2)

    # screen coordinates of farm
    pyautogui.moveTo(850, 525)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # screen coordinates for "Cancel" button
    pyautogui.moveTo(1000, 850)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # screen coordinates for "Yes" button
    pyautogui.moveTo(900, 570)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)
