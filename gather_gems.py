"""
gather_gems.py

Inputs:
    None
    The script will use the gem locations bookmarked as input
    Runs continuously and sends gathering troops to the location in the bookmark list
"""
import time

import pyautogui
import pytesseract

# this is to have time to bring the game window on the top/front
print("Waiting 5 sec")
time.sleep(5)

while(1):
    pyautogui.moveTo(1040, 260)  # bookmark symbol
    print("bookmark")
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    pyautogui.moveTo(1100, 400)  # view button
    print("view")
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    pyautogui.moveTo(850, 525)  # gem lode
    print("gem lode")
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    pyautogui.moveTo(850, 525)  # gather button
    print("gather")
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    # check if army limit allows sending another gathering troops unit
    # if army limit reached, retry after a minute
    while(1):
        pyautogui.screenshot("gather_gems.png", region=(780*2, 510*2, 220, 60))
        text = pytesseract.image_to_string("gather_gems.png").strip().lower()
        print(text)
        if text == "confirm":
            time.sleep(60)

            pyautogui.moveTo(850, 525)  # confirm button
            print("confirm")
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            time.sleep(1)

            pyautogui.moveTo(850, 525)  # gem lode
            print("gem lode")
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            time.sleep(1)

            pyautogui.moveTo(850, 525)  # gather button
            print("gather")
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            time.sleep(1)

        else:
            break

    pyautogui.moveTo(1250, 600)  # lowest tier button
    print("lowest tier")
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    pyautogui.moveTo(1250, 770)  # go button
    print("go")
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(5)

    pyautogui.moveTo(1040, 260)  # bookmark symbol
    print("bookmark")
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    pyautogui.moveTo(1000, 400)  # dustbin button
    print("dustbin")
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    pyautogui.moveTo(1425, 200)  # cross/exit the bookmark window
    print("cross")
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)
