# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import pyautogui

from func.action import *
from func.func import *
from config import settings


def run_bot(name):
    # screen = check_screen()
    # print(screen)
    # exit()
    # Use a breakpoint in the code line below to debug your script.
    while True:
        # try:
        #reload_and_login()
        # end_idle_farm()
        time.sleep(1)
        while True:
            screen = check_screen()
            if screen['name'] == 'home':
                status = start_farm(stage=1, lvl="easy")
                if not status:
                    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", region=(
                        settings['region']['left'], settings['region']['top'], settings['region']['width'],
                        settings['region']['height']), confidence=0.9)
                    pyautogui.click(pos1)
                    time.sleep(1)
                    break
            print(screen)

            time.sleep(1)

        print("Waiting next round")
        # start_idle_farm()
        time.sleep(1)
    # except:
    #     reload_and_login()
    # finally:
    #     pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_bot('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
