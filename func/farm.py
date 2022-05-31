# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import pyautogui

from func.action import *
from func.func import *
from config import settings


def start_farm_account(account=1):
    reload_and_login(account=account)
    time.sleep(3)
    stages = settings['account'][account]['configstage']
    print(stages.keys())
    for stage_full in stages.keys():
        tmp = stage_full.split('-')
        while True:
            screen = check_screen()
            if screen['name'] == 'home':
                status = start_farm(stage=int(tmp[0]), sub_stage=int(tmp[1]), lvl=tmp[2], account=account)
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
