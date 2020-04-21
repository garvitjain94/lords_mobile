"""
open_chests_one.py
- Opens the chests in the bag one by one by clicking the "Use" button.
- Faster method exists using "Stack" button, but watching the chests count go down by 1 is more fun!

Inputs:
    Screen coordinates of "Use" button

Once all chests are open, exit the script by switching to terminal and pressing Ctrl+Z
"""
import time

import pyautogui

# this is to have time to bring the game window on the top/front
print("Waiting 5 sec")
time.sleep(5)

while(1):
    # screen coordinates 0f "Use" button
    pyautogui.moveTo(1070, 40)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)
