"""
enemy_invading_camps.py
- script will keep monitoring the screen for "An Enemy Army is invading your Camp".
- If string is present
    it will start making sound. Please keep speaker volume audible
    Recall all gathering troops

Inputs:
    None

- Runs continuously | Press Ctrl+Z in terminal to stop/reset.
"""
import sys
import time

import pyautogui
import pytesseract
from multiprocessing import Process


def generate_alerting_beeps(count):
    while(count):
        print("\a")
        count -= 1
        time.sleep(0.5)


def press_ReturnToCastle_buttons():
    # screen coordinates of the "Army Status" button
    pyautogui.moveTo(240, 480)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # press "Return to castle" for first gathering troops
    pyautogui.moveTo(1200, 400)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # press "Return to castle" for second gathering troops
    pyautogui.moveTo(1200, 600)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # press "Return to castle" for third gathering troops
    pyautogui.moveTo(1200, 770)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # scroll up for cases when more troops out gathering
    pyautogui.scroll(-10)
    time.sleep(1)

    # check for "Return to Castle" button for fourth gathering troops
    pyautogui.screenshot("Return_to_Castle_4.png",
                         region=(1070*2, 660*2, 348, 60))
    button_str = pytesseract.image_to_string(
        'Return_to_Castle_4.png').split()
    button_str = [i.lower() for i in button_str]
    if "return" in button_str:
        pyautogui.moveTo(1200, 660)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(1)

    # check for "Return to Castle" button for fifth gathering troops
    pyautogui.screenshot("Return_to_Castle_5.png",
                         region=(1070*2, 840*2, 348, 60))
    button_str = pytesseract.image_to_string(
        'Return_to_Castle_5.png').split()
    button_str = [i.lower() for i in button_str]
    if "return" in button_str:
        pyautogui.moveTo(1200, 850)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(1)


def main():

    # this is to have time to bring the game window on the top/front
    print("Waiting 5 sec")
    time.sleep(5)

    while(1):
        # runs every 1 sec
        time.sleep(1)
        # screen coordinates of the message that appear on the game window
        pyautogui.screenshot("enemy_invading_camps.png",
                             region=(580*2, 420*2, 1000, 80))
        message_string = pytesseract.image_to_string(
            'enemy_invading_camps.png').split()
        message_string = [i.lower() for i in message_string]

        # if an enemy starts invading your camp
        #   the script generates 10 beeps
        #   the script recalls at gathering troops from all tiles
        if "invading" in message_string:
            Process(target=generate_alerting_beeps, args=(10,)).start()
            press_ReturnToCastle_buttons()


if __name__ == '__main__':
    main()
