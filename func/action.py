import time

import pyautogui

from func.func import check_screen

config_stage = {
    "3-normal": ["./resources/heroes/kim.png",
                 "./resources/heroes/thuy.png",
                 ],
    "3-easy": ["./resources/heroes/hoa3.png",
               "./resources/heroes/moc3.png",
               "./resources/heroes/thuy3.png",
               ],
    "6-normal": ["./resources/heroes/tho5.png",
                 "./resources/heroes/thuy5.png",
                 "./resources/heroes/moc5.png",
                 "./resources/heroes/moc51.png",
                 "./resources/heroes/moc52.png",
                 ]
}


def go_to_stage(stage=3, lvl="normal"):
    screen = check_screen()
    print(screen)
    if screen['data']['lvl'] != lvl:
        pos1 = pyautogui.locateCenterOnScreen("./resources/stages/" + lvl + "-sm.png", confidence=0.9)
        pyautogui.click(x=pos1.x, y=pos1.y)
        time.sleep(1)
    if screen['data']['stage'] > stage:
        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/prev-btn.png", confidence=0.9)
        pyautogui.click(x=pos1.x, y=pos1.y)
        time.sleep(1)
        return go_to_stage(stage=stage, lvl=lvl)
    elif screen['data']['stage'] < stage:
        pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/next-btn.png", confidence=0.9)
        pyautogui.click(x=pos1.x, y=pos1.y)
        time.sleep(1)
        return go_to_stage(stage=stage, lvl=lvl)
    else:
        return True


def find_heroes(stage=3, lvl="normal"):
    key = str(stage) + "-" + lvl
    for x in config_stage[key]:
        try:
            pos = pyautogui.locateCenterOnScreen(x, confidence=0.9)
            if pos is None:
                continue
            print(pos)
            return pos
        except:
            continue
    return False


def start_farm(stage=3, lvl="normal"):
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/story-btn.png", confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(1)
    go_to_stage(stage=stage, lvl=lvl)
    time.sleep(1)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/" + str(stage) + "-btn.png", confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y - 20)
    time.sleep(1)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/battle-btn1.png", confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(1)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/clear.png", confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(1)
    pos1 = find_heroes(stage=stage, lvl=lvl)
    if not pos1:
        return False
    pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(1)
    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/battle-btn2.png", confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    while True:
        time.sleep(2)
        screen = check_screen()
        if screen['name'] == 'victory':
            break

    pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/home-btn.png", confidence=0.9)
    pyautogui.click(x=pos1.x, y=pos1.y)
    time.sleep(1)
    return True
