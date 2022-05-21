import time

import pyautogui

from func.func import check_screen
from config import settings

config_stage = {
    "1-easy": ["./resources/heroes/thuy115.png",
               "./resources/heroes/kim115.png",
               "./resources/heroes/moc115.png",
               ],
    "3-normal": ["./resources/heroes/kim460.png",
                 "./resources/heroes/thuy460.png",
                 ],
    "3-easy": ["./resources/heroes/hoa340.png",
               "./resources/heroes/moc340.png",
               "./resources/heroes/thuy340.png",
               ],
    "6-normal": ["./resources/heroes/tho585.png",
                 "./resources/heroes/kim585.png",
                 "./resources/heroes/thuy585.png",
                 "./resources/heroes/thuy585.png",
                 "./resources/heroes/thuy570.png",
                 "./resources/heroes/moc564.png",
                 ],
}


def go_to_stage(stage=3, lvl="normal"):
    screen = check_screen()
    print(screen)
    if screen['data']['lvl'] != lvl:
        pos1 = pyautogui.locateCenterOnScreen("./resources/stages/" + lvl + "-sm.png", region=(
            settings['region']['left'], settings['region']['top'], settings['region']['width'],
            settings['region']['height']), confidence=0.9)
        pyautogui.click(pos1)
        time.sleep(0.5)
    if screen['data']['stage'] > stage:
        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/prev-btn.png", region=(
            settings['region']['left'], settings['region']['top'], settings['region']['width'],
            settings['region']['height']), confidence=0.9)
        pyautogui.click(pos1)
        time.sleep(0.5)
        return go_to_stage(stage=stage, lvl=lvl)
    elif screen['data']['stage'] < stage:
        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/next-btn.png", region=(
            settings['region']['left'], settings['region']['top'], settings['region']['width'],
            settings['region']['height']), confidence=0.9)
        pyautogui.click(pos1)
        time.sleep(0.5)
        return go_to_stage(stage=stage, lvl=lvl)
    else:
        return True


def find_heroes(stage=3, lvl="normal"):
    key = str(stage) + "-" + lvl
    for x in config_stage[key]:
        try:
            pos = pyautogui.locateCenterOnScreen(x, region=(
                settings['region']['left'], settings['region']['top'], settings['region']['width'],
                settings['region']['height']), confidence=0.9)
            if pos is None:
                continue
            print(pos)
            return pos
        except:
            continue
    return False


def start_farm(stage=3, lvl="normal"):
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/story-btn.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(pos1)
    time.sleep(3)
    go_to_stage(stage=stage, lvl=lvl)
    time.sleep(3)
    pos2 = pyautogui.locateCenterOnScreen("./resources/buttons/" + str(stage) + "-btn.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(pos2)
    time.sleep(3)
    pos3 = pyautogui.locateCenterOnScreen("./resources/buttons/battle-btn1.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(pos3)
    time.sleep(3)
    pos4 = pyautogui.locateCenterOnScreen("./resources/buttons/clear.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(pos4)
    time.sleep(2)
    pos5 = find_heroes(stage=stage, lvl=lvl)
    if not pos5:
        return False
    print('heroes')
    print(pos5)
    pyautogui.click(pos5)
    pos = pyautogui.locateCenterOnScreen("./resources/buttons/battle-btn2.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    print(pos)
    time.sleep(3)
    pyautogui.moveTo(pos)
    a = pyautogui.click()
    print(a)
    time.sleep(3)
    while True:
        time.sleep(3)
        screen = check_screen()
        if screen['name'] == 'victory':
            print(screen)
            break

    pos6 = pyautogui.locateCenterOnScreen("./resources/buttons/home-btn.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(pos6)
    time.sleep(2)
    return True


def reload_and_login():
    print("Start login")
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/reload-btn.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(20)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/login-input.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    pyautogui.write(settings['password'])
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/login-btn.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(1)
    while True:
        screen = check_screen()
        print(screen)
        if screen['name'] == 'home':
            break
    print("Login success")
    return True


def start_idle_farm():
    print("Start idle")
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/idle-btn.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(2)

    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/add-btn.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    if pos1 is None:
        return False
    pyautogui.click(x=pos1.x, y=pos1.y)

    x = settings['start_idle_x']
    y = settings['start_idle_y']

    pyautogui.click(x=x, y=y)
    time.sleep(1)
    pyautogui.click(x=x + 105 * 1, y=y)
    time.sleep(1)
    pyautogui.click(x=x + 105 * 2, y=y)
    time.sleep(1)
    pyautogui.click(x=x + 105 * 3, y=y)
    time.sleep(1)
    pyautogui.click(x=x, y=y + 100)
    time.sleep(10)

    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/confirm-btn.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)

    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(1)
    while True:
        screen = check_screen()
        print(screen)
        if screen['name'] == 'home':
            break
    print("End idle")
    return True


def end_idle_farm():
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/idle-btn.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(2)
    pos1 = pyautogui.locateCenterOnScreen("./resources/screens/idle.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    status = True
    if pos1 is None:
        print("Idle can not claim")
    else:
        print("Idle can claim")
        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/claim-btn.png", region=(
            settings['region']['left'], settings['region']['top'], settings['region']['width'],
            settings['region']['height']), confidence=0.9)
        pyautogui.click(x=pos1.x, y=pos1.y)
        time.sleep(1)
        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/ok-btn.png", region=(
            settings['region']['left'], settings['region']['top'], settings['region']['width'],
            settings['region']['height']), confidence=0.9)
        pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(1)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(1)
    while True:
        screen = check_screen()
        print(screen)
        if screen['name'] == 'home':
            break
    return True
