import pyautogui
import platform


def custom_click(x, y):
    system_name = platform.system()
    if system_name == "Linux":
        pyautogui.click(x=x, y=y)
        return True
    if system_name == "Windows":
        pyautogui.moveTo(x=x, y=y)
        pyautogui.sleep(1)
        pyautogui.click()
        return True
    if system_name == "Macos":
        pyautogui.click(x=x/2, y=y/2)
        return True
    