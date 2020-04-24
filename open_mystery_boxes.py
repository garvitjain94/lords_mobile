"""
open_mystery_boxes.py
- script will keep monitoring the screen for the mystery box to be collected. Once available, it gets the reward.

Inputs:
    None

- Runs continuously | Press Ctrl+Z in terminal to stop/reset.
"""
import time

import pyautogui

while(1):
    if pyautogui.locateOnScreen('open_mystery_box_str.png', confidence=0.6):
        print("Opening mystery box!")

        # click the mystery box
        pyautogui.moveTo(1336, 717)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(1)

        # click the reward button
        pyautogui.moveTo(750, 750)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(1)
