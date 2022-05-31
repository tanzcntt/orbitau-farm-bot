import time

import pyautogui

from func.func import check_screen
from config import settings


def go_to_stage(stage=3, lvl="normal"):
    screen = check_screen()
    print(screen)
    if screen['data']['lvl'] != lvl:
        pos1 = pyautogui.locateCenterOnScreen("./resources/stages/" + lvl + "-sm.png", region=(
            settings['region']['left'], settings['region']['top'], settings['region']['width'],
            settings['region']['height']), confidence=0.9)
        pyautogui.click(x=pos1.x, y=pos1.y)
        time.sleep(0.5)
    if screen['data']['stage'] > stage:
        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/prev-btn.png", region=(
            settings['region']['left'], settings['region']['top'], settings['region']['width'],
            settings['region']['height']), confidence=0.9)
        pyautogui.click(x=pos1.x, y=pos1.y)
        time.sleep(0.5)
        return go_to_stage(stage=stage, lvl=lvl)
    elif screen['data']['stage'] < stage:
        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/next-btn.png", region=(
            settings['region']['left'], settings['region']['top'], settings['region']['width'],
            settings['region']['height']), confidence=0.9)
        pyautogui.click(x=pos1.x, y=pos1.y)
        time.sleep(0.5)
        return go_to_stage(stage=stage, lvl=lvl)
    else:
        return True


def find_heroes(stage=3, sub_stage=1, lvl="normal", account=1):
    key = str(stage) + "-" + str(sub_stage) + "-" + lvl
    config_stage = settings['account'][account]['configstage']
    for x in config_stage[key]:
        try:
            confidence = 0.9
            if lvl == 'hard':
                confidence = 0.96
            pos = pyautogui.locateCenterOnScreen(x, region=(
                settings['region']['left'], settings['region']['top'], settings['region']['width'],
                settings['region']['height']), confidence=confidence)
            if pos is None:
                continue
            print(pos)
            return pos
        except:
            continue
    return False


def start_farm(stage=3, sub_stage=1, lvl="normal", account=1):
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/story-btn.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(1)
    go_to_stage(stage=stage, lvl=lvl)
    time.sleep(1)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/" + str(stage) + "-" + str(sub_stage) + ".png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y - 20)
    time.sleep(1)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/battle-btn1.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(1)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/clear.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    pos1 = find_heroes(stage=stage, sub_stage=sub_stage, lvl=lvl, account=account)
    if not pos1:
        return False
    pyautogui.click(x=pos1.x, y=pos1.y)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/battle-btn2.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    while True:
        pos_home_btn = pyautogui.locateCenterOnScreen("./resources/buttons/home-victory-btn.png", region=(
            settings['region']['left'], settings['region']['top'], settings['region']['width'],
            settings['region']['height']), confidence=0.9)
        if pos_home_btn is not None:
            break
        pos_home_btn = pyautogui.locateCenterOnScreen("./resources/buttons/home-defeat-btn.png", region=(
            settings['region']['left'], settings['region']['top'], settings['region']['width'],
            settings['region']['height']), confidence=0.9)
        if pos_home_btn is not None:
            break

    pyautogui.click(x=pos_home_btn.x, y=pos_home_btn.y)
    return True


def reload_and_login(account=1):
    print("Start login")
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/reload-btn.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(10)

    pyautogui.click(x=settings['login']['userpos']['x'], y=settings['login']['userpos']['y'])
    pyautogui.write(settings['account'][account]['username'])
    time.sleep(1)
    pyautogui.click(x=settings['login']['passpos']['x'], y=settings['login']['passpos']['y'])
    pyautogui.write(settings['account'][account]['password'])
    time.sleep(1)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/login-btn.png", region=(
        settings['region']['left'], settings['region']['top'], settings['region']['width'],
        settings['region']['height']),
                                          confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    while True:
        screen = check_screen()
        print(screen)
        if screen['name'] == 'home':
            break
    print("Login success")
    return True


def start_idle_farm(account=1):
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

    heroes_count = 0
    list_pos = []
    config_idle = settings['account'][account]['config_idle']
    for h in config_idle:
        ph = list(pyautogui.locateAllOnScreen(h, region=(
            settings['region']['left'], settings['region']['top'], settings['region']['width'],
            settings['region']['height']), confidence=0.9))
        list_pos = list_pos + ph
    for box in list_pos:
        if heroes_count >= 5:
            break
        pos = pyautogui.center(box)
        pyautogui.click(x=pos.x, y=pos.y)
        time.sleep(1)
        heroes_count = heroes_count + 1
    if heroes_count < 5:
        start_drag_x = (settings['region']['left'] + settings['region']['width'] / 2)
        start_drag_y = (settings['region']['top'] + settings['region']['height'] / 2)
        pyautogui.moveTo(x=start_drag_x, y=start_drag_y)
        pyautogui.dragTo(x=start_drag_x, y=start_drag_y - 200, duration=2, button='left')
        time.sleep(3)
        list_pos2 = []
        for h in config_idle:
            ph = list(pyautogui.locateAllOnScreen(h, region=(
                settings['region']['left'], settings['region']['top'], settings['region']['width'],
                settings['region']['height']), confidence=0.9))
            list_pos2 = list_pos2 + ph
        for box in list_pos2:
            if heroes_count >= 5:
                break
            pos = pyautogui.center(box)
            pyautogui.click(x=pos.x, y=pos.y)
            time.sleep(1)
            heroes_count = heroes_count + 1
        start_drag_x = (settings['region']['left'] + settings['region']['width'] / 2)
        start_drag_y = (settings['region']['top'] + settings['region']['height'] / 2)
        pyautogui.moveTo(x=start_drag_x, y=start_drag_y)
        pyautogui.dragTo(x=start_drag_x, y=start_drag_y + 200, duration=2, button='left')
        time.sleep(3)

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
    while True:
        time.sleep(1)
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
    while True:
        screen = check_screen()
        print(screen)
        if screen['name'] == 'home':
            break
    return True
