import pyautogui


def check_screen():
    try:
        if pyautogui.locateOnScreen("./resources/screens/victory.png", confidence=0.9):
            return {
                "name": "victory",
                "data": {}
            }
    except:
        pass
    # try:
    #     if pyautogui.locateOnScreen("./resources/screens/battling.png", confidence=0.9):
    #         return {
    #             "name": "battling",
    #             "data": {}
    #         }
    # except:
    #     pass
    try:
        if pyautogui.locateOnScreen("./resources/screens/battle.png", confidence=0.9):
            return {
                "name": "battle",
                "data": {}
            }
    except:
        pass
    try:
        if pyautogui.locateOnScreen("./resources/screens/formation.png", confidence=0.9):
            lvl = "easy"
            return {
                "name": "formation",
                "data": {}
            }
    except:
        pass
    try:
        if pyautogui.locateOnScreen("./resources/screens/home.png", confidence=0.9):
            return {
                "name": "home",
                "data": {}
            }
    except:
        pass
    try:
        if pyautogui.locateOnScreen("./resources/screens/story.png", confidence=0.9):
            stage = 1
            lvl = "easy"
            if pyautogui.locateOnScreen("./resources/stages/1.png", confidence=0.9):
                stage = 1
            elif pyautogui.locateOnScreen("./resources/stages/2.png", confidence=0.9):
                stage = 2
            elif pyautogui.locateOnScreen("./resources/stages/3.png", confidence=0.9):
                stage = 3
            elif pyautogui.locateOnScreen("./resources/stages/4.png", confidence=0.9):
                stage = 4
            elif pyautogui.locateOnScreen("./resources/stages/5.png", confidence=0.9):
                stage = 5
            elif pyautogui.locateOnScreen("./resources/stages/6.png", confidence=0.9):
                stage = 6

            if pyautogui.locateOnScreen("./resources/stages/easy.png", confidence=0.9):
                lvl = "easy"
            elif pyautogui.locateOnScreen("./resources/stages/normal.png", confidence=0.9):
                lvl = "normal"
            elif pyautogui.locateOnScreen("./resources/stages/hard.png", confidence=0.9):
                lvl = "hard"
            elif pyautogui.locateOnScreen("./resources/stages/hell.png", confidence=0.9):
                lvl = "hell"

            return {
                "name": "story",
                "data": {
                    "lvl": lvl,
                    "stage": stage
                }
            }
    except:
        pass

    return {
        "name": "404",
        "data": {}
    }
