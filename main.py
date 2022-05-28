# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import pyautogui

from func.action import *
from func.func import *
from config import settings


def start_farm_account1():
    reload_and_login(account=1)
    end_idle_farm()
    time.sleep(1)
    while True:
        screen = check_screen()
        if screen['name'] == 'home':
            status = start_farm(stage=2, sub_stage=10, lvl="hard", account=1)
            if not status:
                pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", region=(
                    settings['region']['left'], settings['region']['top'], settings['region']['width'],
                    settings['region']['height']), confidence=0.9)
                pyautogui.click(x=pos1.x, y=pos1.y)
                time.sleep(1)
                break
        print(screen)
        # pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", region=(settings['region']['left'], settings['region']['top'], settings['region']['width'], settings['region']['height']), confidence=0.9)
        # pyautogui.click(x=pos1.x, y=pos1.y)
        time.sleep(1)
    while True:
        screen = check_screen()
        if screen['name'] == 'home':
            status = start_farm(stage=6, sub_stage=1, lvl="normal", account=1)
            if not status:
                pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", region=(
                    settings['region']['left'], settings['region']['top'], settings['region']['width'],
                    settings['region']['height']), confidence=0.9)
                pyautogui.click(x=pos1.x, y=pos1.y)
                time.sleep(1)
                break
        print(screen)
        # pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", region=(settings['region']['left'], settings['region']['top'], settings['region']['width'], settings['region']['height']), confidence=0.9)
        # pyautogui.click(x=pos1.x, y=pos1.y)
        time.sleep(1)

    while True:
        screen = check_screen()
        if screen['name'] == 'home':
            status = start_farm(stage=3, sub_stage=1, lvl="normal", account=1)
            if not status:
                pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", region=(
                    settings['region']['left'], settings['region']['top'], settings['region']['width'],
                    settings['region']['height']), confidence=0.9)
                pyautogui.click(x=pos1.x, y=pos1.y)
                time.sleep(1)
                break
        print(screen)
        # pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", region=(settings['region']['left'], settings['region']['top'], settings['region']['width'], settings['region']['height']), confidence=0.9)
        # pyautogui.click(x=pos1.x, y=pos1.y)
        time.sleep(1)
    while True:
        screen = check_screen()
        if screen['name'] == 'home':
            status = start_farm(stage=3, sub_stage=1, lvl="easy", account=1)
            if not status:
                pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", region=(
                    settings['region']['left'], settings['region']['top'], settings['region']['width'],
                    settings['region']['height']), confidence=0.9)
                pyautogui.click(x=pos1.x, y=pos1.y)
                time.sleep(1)
                break
        print(screen)
        # pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", region=(settings['region']['left'], settings['region']['top'], settings['region']['width'], settings['region']['height']), confidence=0.9)
        # pyautogui.click(x=pos1.x, y=pos1.y)
        time.sleep(1)
    print("Waiting next round")
    start_idle_farm(account=1)
    time.sleep(1)


def start_farm_account2():
    reload_and_login(account=2)
    time.sleep(3)
    while True:
        screen = check_screen()
        if screen['name'] == 'home':
            status = start_farm(stage=1, sub_stage=1, lvl="easy", account=2)
            if not status:
                pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", region=(
                    settings['region']['left'], settings['region']['top'], settings['region']['width'],
                    settings['region']['height']), confidence=0.9)
                pyautogui.click(x=pos1.x, y=pos1.y)
                time.sleep(1)
                break
        print(screen)
        time.sleep(1)
    # while True:
    #     screen = check_screen()
    #     if screen['name'] == 'home':
    #         status = start_farm(stage=2, sub_stage=1, lvl="easy", account=2)
    #         if not status:
    #             pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", region=(
    #                 settings['region']['left'], settings['region']['top'], settings['region']['width'],
    #                 settings['region']['height']), confidence=0.9)
    #             pyautogui.click(x=pos1.x, y=pos1.y)
    #             time.sleep(1)
    #             break
    #     print(screen)
    #     time.sleep(1)

    while True:
        screen = check_screen()
        if screen['name'] == 'home':
            status = start_farm(stage=3, sub_stage=1, lvl="easy", account=2)
            if not status:
                pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", region=(
                    settings['region']['left'], settings['region']['top'], settings['region']['width'],
                    settings['region']['height']), confidence=0.9)
                pyautogui.click(x=pos1.x, y=pos1.y)
                time.sleep(1)
                break
        print(screen)
        time.sleep(1)

    print("Waiting next round")
    time.sleep(1)


def run_bot(name):
    # start_idle_farm()
    # exit()
    # Use a breakpoint in the code line below to debug your script.
    while True:

        # start_farm_account2()
        try:
            start_farm_account2()
            start_farm_account1()
        except Exception:
            reload_and_login(account=1)
        finally:
            pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_bot('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
