# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import pyautogui

from func.action import *
from func.func import *
from config import settings


def start_farm_account3():
    reload_and_login(account=3)
    time.sleep(3)
    while True:
        screen = check_screen()
        if screen['name'] == 'home':
            status = start_farm(stage=1, sub_stage=10, lvl="normal", account=3)
            if not status:
                pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", region=(
                    settings['region']['left'], settings['region']['top'], settings['region']['width'],
                    settings['region']['height']), confidence=0.9)
                pyautogui.click(x=pos1.x, y=pos1.y)
                time.sleep(1)
                break
        print(screen)
        time.sleep(1)

    while True:
        screen = check_screen()
        if screen['name'] == 'home':
            status = start_farm(stage=5, sub_stage=1, lvl="easy", account=3)
            if not status:
                pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", region=(
                    settings['region']['left'], settings['region']['top'], settings['region']['width'],
                    settings['region']['height']), confidence=0.9)
                pyautogui.click(x=pos1.x, y=pos1.y)
                time.sleep(1)
                break
        print(screen)
        time.sleep(1)

    while True:
        screen = check_screen()
        if screen['name'] == 'home':
            status = start_farm(stage=4, sub_stage=10, lvl="easy", account=3)
            if not status:
                pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", region=(
                    settings['region']['left'], settings['region']['top'], settings['region']['width'],
                    settings['region']['height']), confidence=0.9)
                pyautogui.click(x=pos1.x, y=pos1.y)
                time.sleep(1)
                break
        print(screen)
        time.sleep(1)

    while True:
        screen = check_screen()
        if screen['name'] == 'home':
            status = start_farm(stage=2, sub_stage=1, lvl="easy", account=3)
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
