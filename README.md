# lords_mobile

This repo will house python scripts for automating tasks in the LORDS MOBILE mobile game. Have started with pyautogui module to automate clicks on the screen.The first script hit_monster.py has been developed on my mac and hence hard coded values can be found. 

INSPIRATION: During guild fest, we often land at tasks like hit monsters. I use this opportunity to increase EXP of heroes which haven't maxed out yet...which means 8-10 hits per lvl1 monster. Doing this manually seems mundane and hence the source of inspiration.

REQUIREMENTS:
- python3 installation : https://realpython.com/installing-python/
- pyautogui module installation : In terminal enter the following command
    - pip install PyAutoGUI
- Bluestacks installation : https://www.bluestacks.com/
    - Android gaming platform for PC

PREREQUISITES:
- Launch Bluestacks
- Launch Lords Mobile app
- Run the python script in a terminal. 
- Switch to the game window. The scripts have buffer at start to allow switching from terminal to game window.

Tip : I do not resize/move the bluestack window for ease of scripts to work. Eg. As per my mac, the screen coordinates for the center of the bluestacks window is (x=850, y=525). I make sure to bring turf item at these coordinates, to ensure the script works seemlessly every time.

TODO:
- Send help automation : If a guild member gets a task to send helps, a script should continuously put a building in upgrade, ask for help and cancel upgrade repeatedly. Planning to use pyautogui again.