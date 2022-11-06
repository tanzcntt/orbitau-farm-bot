import time
import traceback

import pyautogui

from func.click import custom_click
from func.func import check_screen
from config import settings


def go_to_stage(screen, stage=3, lvl="normal"):
    screenx = check_screen(screen)
    print(screenx)
    if screenx['data']['lvl'] != lvl:
        pos1 = pyautogui.locateCenterOnScreen("./resources/stages/" + lvl + "-sm.png", region=(
            settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
            settings[screen]['region']['height']), confidence=0.85)
        custom_click(x=pos1.x, y=pos1.y)
        time.sleep(0.5)
    if screenx['data']['stage'] > stage:
        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/prev-btn.png", region=(
            settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
            settings[screen]['region']['height']), confidence=0.9)
        custom_click(x=pos1.x, y=pos1.y)
        time.sleep(0.5)
        return go_to_stage(screen, stage=stage, lvl=lvl)
    elif screenx['data']['stage'] < stage:
        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/next-btn.png", region=(
            settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
            settings[screen]['region']['height']), confidence=0.9)
        custom_click(x=pos1.x, y=pos1.y)
        time.sleep(0.5)
        return go_to_stage(screen, stage=stage, lvl=lvl)
    else:
        return True


def find_heroes(screen, stage=3, sub_stage=1, lvl="normal", account=1):
    key = str(stage) + "-" + str(sub_stage) + "-" + lvl
    config_stage = settings[screen]['account'][account]['configstage']
    for x in config_stage[key]:
        try:
            confidence = 0.89
            pos = pyautogui.locateCenterOnScreen(x, region=(
                settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
                settings[screen]['region']['height']), confidence=confidence)
            if pos is None:
                continue
            print(pos)
            return pos
        except Exception as e:
            print(e)
            traceback.print_exc()
            pass
    return False


def start_farm(screen, stage=3, sub_stage=1, lvl="normal", account=1):
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/story-btn.png", region=(
        settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
        settings[screen]['region']['height']),
                                          confidence=0.9)
    custom_click(x=pos1.x, y=pos1.y)
    time.sleep(1)
    go_to_stage(screen, stage=stage, lvl=lvl)
    time.sleep(1)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/" + str(stage) + "-" + str(sub_stage) + ".png", region=(
        settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
        settings[screen]['region']['height']),
                                          confidence=0.9)
    if stage == 6:
        custom_click(x=pos1.x, y=pos1.y - 50)
    else:
        custom_click(x=pos1.x, y=pos1.y - 20)

    time.sleep(1)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/battle-btn1.png", region=(
        settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
        settings[screen]['region']['height']),
                                          confidence=0.9)
    custom_click(x=pos1.x, y=pos1.y)
    time.sleep(1)

    while True:
        time.sleep(1)
        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/clear.png", region=(
            settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
            settings[screen]['region']['height']),
                                              confidence=0.9)
        custom_click(x=pos1.x, y=pos1.y)
        time.sleep(1)
        pos1 = find_heroes(screen, stage=stage, sub_stage=sub_stage, lvl=lvl, account=account)
        if not pos1:
            return False
        custom_click(x=pos1.x, y=pos1.y)
        time.sleep(1)
        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/battle-btn2.png", region=(
            settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
            settings[screen]['region']['height']),
                                              confidence=0.9)
        custom_click(x=pos1.x, y=pos1.y)
        time.sleep(0.5)
        total_not_end = 1
        while True:
            if total_not_end > 300:
                raise Exception("Unknown error")
            pos_skip = pyautogui.locateCenterOnScreen("./resources/buttons/skip-btn.png", region=(
                settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
                settings[screen]['region']['height']), confidence=0.9)
            if pos_skip is not None:
                custom_click(x=pos_skip.x, y=pos_skip.y)
                time.sleep(1)
            pos_play_again = pyautogui.locateCenterOnScreen("./resources/buttons/playagain-btn.png", region=(
                settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
                settings[screen]['region']['height']), confidence=0.9)
            if pos_play_again is not None:
                custom_click(x=pos_play_again.x, y=pos_play_again.y)
                time.sleep(1)
                break
            pos_play_again = pyautogui.locateCenterOnScreen("./resources/buttons/playagain-btn2.png", region=(
                settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
                settings[screen]['region']['height']), confidence=0.9)
            if pos_play_again is not None:
                custom_click(x=pos_play_again.x, y=pos_play_again.y)
                time.sleep(1)
                break
            time.sleep(1)
            total_not_end = total_not_end + 1


def reload_and_login(screen, account=1):
    print("Start login")
    # time.sleep(10)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/reload-btn.png", region=(
        settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
        settings[screen]['region']['height']),
                                          confidence=0.9)
    custom_click(x=pos1.x, y=pos1.y)
    time.sleep(10)

    custom_click(x=settings[screen]['login']['userpos']['x'], y=settings[screen]['login']['userpos']['y'])
    time.sleep(1)
    for x in range(40):
        pyautogui.press('backspace')
        pyautogui.press('delete')
    time.sleep(1)
    pyautogui.write(settings[screen]['account'][account]['username'])
    time.sleep(1)
    custom_click(x=settings[screen]['login']['passpos']['x'], y=settings[screen]['login']['passpos']['y'])
    pyautogui.write(settings[screen]['account'][account]['password'])
    time.sleep(1)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/login-btn.png", region=(
        settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
        settings[screen]['region']['height']),
                                          confidence=0.9)
    custom_click(x=pos1.x, y=pos1.y)
    total_not_end = 1
    while True:
        if total_not_end > 100:
            raise Exception("Unknown error")
        screenx = check_screen(screen)
        print(screenx)
        time.sleep(1)
        if screenx['name'] == 'home':
            break
        total_not_end = total_not_end + 1
    print("Login success")
    return True


def start_idle_farm(screen, account=1):
    print("Start idle")
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/idle-btn.png", region=(
        settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
        settings[screen]['region']['height']),
                                          confidence=0.9)
    custom_click(x=pos1.x, y=pos1.y)
    time.sleep(2)

    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/add-btn.png", region=(
        settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
        settings[screen]['region']['height']),
                                          confidence=0.9)
    if pos1 is None:
        return False
    custom_click(x=pos1.x, y=pos1.y)

    heroes_count = 0
    list_pos = []
    config_idle = settings[screen]['account'][account]['config_idle']
    for h in config_idle:
        ph = list(pyautogui.locateAllOnScreen(h, region=(
            settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
            settings[screen]['region']['height']), confidence=0.9))
        list_pos = list_pos + ph
    for box in list_pos:
        if heroes_count >= 5:
            break
        pos = pyautogui.center(box)
        custom_click(x=pos.x, y=pos.y)
        time.sleep(1)
        heroes_count = heroes_count + 1
    if heroes_count < 5:
        start_drag_x = (settings[screen]['region']['left'] + settings[screen]['region']['width'] / 2)
        start_drag_y = (settings[screen]['region']['top'] + settings[screen]['region']['height'] / 2)
        pyautogui.moveTo(x=start_drag_x, y=start_drag_y)
        pyautogui.dragTo(x=start_drag_x, y=start_drag_y - 200, duration=2, button='left')
        time.sleep(3)
        list_pos2 = []
        for h in config_idle:
            ph = list(pyautogui.locateAllOnScreen(h, region=(
                settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
                settings[screen]['region']['height']), confidence=0.9))
            list_pos2 = list_pos2 + ph
        for box in list_pos2:
            if heroes_count >= 5:
                break
            pos = pyautogui.center(box)
            custom_click(x=pos.x, y=pos.y)
            time.sleep(1)
            heroes_count = heroes_count + 1
        start_drag_x = (settings[screen]['region']['left'] + settings[screen]['region']['width'] / 2)
        start_drag_y = (settings[screen]['region']['top'] + settings[screen]['region']['height'] / 2)
        pyautogui.moveTo(x=start_drag_x, y=start_drag_y)
        pyautogui.dragTo(x=start_drag_x, y=start_drag_y + 200, duration=2, button='left')
        time.sleep(3)

    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/confirm-btn.png", region=(
        settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
        settings[screen]['region']['height']),
                                          confidence=0.9)
    custom_click(x=pos1.x, y=pos1.y)

    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", region=(
        settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
        settings[screen]['region']['height']),
                                          confidence=0.9)
    custom_click(x=pos1.x, y=pos1.y)
    while True:
        time.sleep(1)
        screenx = check_screen(screen)
        print(screenx)
        if screenx['name'] == 'home':
            break
    print("End idle")
    return True


def end_idle_farm(screen):
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/idle-btn.png", region=(
        settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
        settings[screen]['region']['height']),
                                          confidence=0.9)
    custom_click(x=pos1.x, y=pos1.y)
    time.sleep(2)
    pos1 = pyautogui.locateCenterOnScreen("./resources/screens/idle.png", region=(
        settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
        settings[screen]['region']['height']),
                                          confidence=0.9)
    if pos1 is None:
        print("Idle can not claim")
    else:
        print("Idle can claim")
        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/claim-btn.png", region=(
            settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
            settings[screen]['region']['height']), confidence=0.9)
        custom_click(x=pos1.x, y=pos1.y)
        time.sleep(1)
        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/ok-btn.png", region=(
            settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
            settings[screen]['region']['height']), confidence=0.9)
        custom_click(x=pos1.x, y=pos1.y)
    time.sleep(1)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", region=(
        settings[screen]['region']['left'], settings[screen]['region']['top'], settings[screen]['region']['width'],
        settings[screen]['region']['height']),
                                          confidence=0.9)
    custom_click(x=pos1.x, y=pos1.y)
    while True:
        screenx = check_screen(screen)
        print(screenx)
        if screenx['name'] == 'home':
            break
    return True
