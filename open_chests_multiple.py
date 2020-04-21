"""
open_chests_multiple.py
- Opens the chests in the bag (upto 100) by clicking the "Stack" button.
- Doesn't work if number of chests is one as no "Stack" button. Manually open those chests before running this script.

Inputs:
    Screen coordinates of "Stack" button

Once all chests are open, exit the script by switching to terminal and pressing Ctrl+Z
"""
import time

import pyautogui

# this is to have time to bring the game window on the top/front
print("Waiting 5 sec")
time.sleep(5)

while(1):
    # screen coordinates 0f "Use" button
    pyautogui.moveTo(1070, 450)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # screen coordinates for "Open" button
    pyautogui.moveTo(910, 720)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # screen coordinates for pressing X in the upper right corner to return to bag window | Chest tab
    pyautogui.moveTo(1400, 200)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)
