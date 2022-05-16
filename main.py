# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import pyautogui

from func.action import *
from func.func import *
from config import settings


def run_bot(name):
    # Use a breakpoint in the code line below to debug your script.
    while True:
        reload_and_login()
        end_idle_farm()
        time.sleep(10)
        while True:
            screen = check_screen()
            if screen['name'] == 'home':
                status = start_farm(stage=6, lvl="normal")
                if not status:
                    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", confidence=0.9)
                    pyautogui.click(x=pos1.x, y=pos1.y)
                    time.sleep(1)
                    break
            print(screen)
            # pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", confidence=0.9)
            # pyautogui.click(x=pos1.x, y=pos1.y)
            time.sleep(1)

        while True:
            screen = check_screen()
            if screen['name'] == 'home':
                status = start_farm(stage=3, lvl="normal")
                if not status:
                    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", confidence=0.9)
                    pyautogui.click(x=pos1.x, y=pos1.y)
                    time.sleep(1)
                    break
            print(screen)
            # pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", confidence=0.9)
            # pyautogui.click(x=pos1.x, y=pos1.y)
            time.sleep(1)
        while True:
            screen = check_screen()
            if screen['name'] == 'home':
                status = start_farm(stage=3, lvl="easy")
                if not status:
                    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", confidence=0.9)
                    pyautogui.click(x=pos1.x, y=pos1.y)
                    time.sleep(1)
                    break
            print(screen)
            # pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", confidence=0.9)
            # pyautogui.click(x=pos1.x, y=pos1.y)
            time.sleep(1)
        print("Waiting next round")
        start_idle_farm()
        time.sleep(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_bot('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
