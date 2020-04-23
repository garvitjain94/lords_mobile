# lords_mobile

This repo will house python scripts for automating tasks in the LORDS MOBILE mobile game. Have started with pyautogui module to automate clicks on the screen.The first script hit_monster.py has been developed on my mac and hence hard coded values can be found. 

INSPIRATION: The following tasks were identified as potential good candidates for automation, and perhaps reduce constant manual instructions:
- During guild fest, we often land at tasks like hit monsters. I use this opportunity to increase EXP of heroes which haven't maxed out yet...which means 8-10 hits per monster. All clicks based execution, so could be automated.
- One of the quests in guild fest is send helps. Guild members can help each other by generating helps thereby speeding up the process of completion of the task. So the member who gets the task of "send help" needs to constantly press "Help All" button. The guild members helping need to first put a building to upgrade, ask for help and then cancel the upgrade. So much clicking could be easily automated.
- Especially during KvK, players relying on resources gathering for points need to constantly monitor the troops out on gathering to avoid any wounded/dead soldiers in case of an attack. Getting audio alerts in such scenarios means no more such worries. Poof!

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

PROGRESS SO FAR:
- hit_monster.py
    - Use to hit monster
- open_chests_one.py
    - Use to open chests one by one | Faster method exists using "Stack" button, but watching the chests count go down by 1 is more fun!
- open_chests_multiple.py
    - Less fun :). Use to open the chests in the bag (upto 100).
- send_help_quest.py
    - Use for "Send Help" quest during guild fest | For players who have taken up "Send Help" quest.
- generate_helps.py
    - Use to generate helps which a guild member can use to complete "Send Help" quest without straining your fingers.
    - Performance : 120 helps takes 10 minutes approx.
    - Note : A player who gets "Send Help" quest should run send_help_quest.py & the other player, who want to help with this task, should run generate_helps.py
enemy_invading_turf.py
- During KvK, don't let enemy attack your resource gathering troops. Gather in peace!
- Script will keep monitoring the screen for "An Enemy Army is invading your Turf". 
- If string is present, it will start making sound. Please keep speaker volume audible.
 