"""
enemy_invading_turf.py
- script will keep monitoring the screen for "An Enemy Army is invading your Turf". 
- If string is present, it will start making sound. Please keep speaker volume audible.
 
Inputs:
    None

- Runs continuously | Press Ctrl+Z in terminal to stop/reset.
- In case script throws error wrt "confidence" parameter below, run
    >> pip install opencv-python
"""
import sys
import time

import pyautogui

while(1):
    if pyautogui.locateOnScreen('images/enemy_invading_turf.png', confidence=0.6):
        print("An Enemy Army is invading your Turf")
        sys.stdout.write('\a')
