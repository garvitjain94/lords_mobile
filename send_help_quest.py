"""
send_help_quest.py
- Keep pressing "Help All" button
- Useful when doing "send help" quest

Inputs:
    Screen coordinates of "Help All" button

Ensure "Send Help" window is open before running this script
Runs continuously | Press Ctrl+Z in terminal once target helps achieved.
"""
import time

import pyautogui

# this is to have time to bring the game window on the top/front
print("Waiting 5 sec")
time.sleep(5)

while(1):
    # screen coordinates 0f "Help All" button
    pyautogui.moveTo(750, 850)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)
