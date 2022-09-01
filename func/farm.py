# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from func.action import *
from func.func import *
from config import settings
from func.click import custom_click


def start_farm_account(screen, account=1):
    reload_and_login(screen, account=account)
    time.sleep(3)
    stages = settings[screen]['account'][account]['configstage']
    # try:
    #     config_idle = settings[screen]['account'][account]['config_idle']
    #     print(config_idle)
    #     if config_idle:
    #         end_idle_farm()
    # except Exception as e:
    #     pass
    print(stages.keys())
    re_run = 0
    while re_run < 1:
        re_run = re_run + 1
        for stage_full in stages.keys():
            tmp = stage_full.split('-')
            total_not_home = 1
            while True:
                if total_not_home > 100:
                    raise Exception("Unknown error")
                screenx = check_screen(screen)
                if screenx['name'] == 'home':
                    status = start_farm(screen, stage=int(tmp[0]), sub_stage=int(tmp[1]), lvl=tmp[2], account=account)
                    if not status:
                        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", region=(
                            settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
                            settings[screen]['region']['height']), confidence=0.9)
                        custom_click(x=pos1.x, y=pos1.y)
                        time.sleep(1)
                        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", region=(
                            settings[screen]['region']['left'], settings[screen]['region']['top'],
                            settings[screen]['region']['width'],
                            settings[screen]['region']['height']), confidence=0.9)
                        custom_click(x=pos1.x, y=pos1.y)
                        time.sleep(1)
                        break
                print(screenx)
                total_not_home = total_not_home + 1
                time.sleep(1)

    # try:
    #     config_idle = settings[screen]['account'][account]['config_idle']
    #     if config_idle:
    #         start_idle_farm(account=account)
    # except:
    #     pass
    print("Waiting next round")
    time.sleep(1)
