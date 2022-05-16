# orbitau-farm-bot
Bot farm đá và uOri cho game Orbitau.io

# Cài dặt

Tải và cài đặt PyCharm CE

Clone code & cài đặt thư viên

Pyautogui

Cpencv-python

Thay các button tương ứng theo tài khoản game, theo kích thước màn hình mọi người, hình hiện tại mình đang cho game chạy ở độ phân giản 1280x1088px

Chụp hình tất cả các hero của bạn

 Sửa config các ải trong func/action.py sẽ farm theo mẫu sau

 ```python

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
```
Như cấu hình trên mình có 2 hero farm solo ở map 3.1 normal, 3 hero farm solo ở map 3.1 ez, 5 hero farm solo ở 6.1 normal

# Sửa lại file main chạy bao nhiều ải tuỳ vào account của bạn
```python
while True:
        screen = check_screen()
        if screen['name'] == 'home':
            status = start_farm(stage=6, lvl="normal")
            if not status:
                pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", confidence=0.9)
                pyautogui.click(x=pos1.x, y=pos1.y)
                time.sleep(1)
                break
        print(screen)
        # pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", confidence=0.9)
        # pyautogui.click(x=pos1.x, y=pos1.y)
        time.sleep(1)

    while True:
        screen = check_screen()
        if screen['name'] == 'home':
            status = start_farm(stage=3, lvl="normal")
            if not status:
                pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", confidence=0.9)
                pyautogui.click(x=pos1.x, y=pos1.y)
                time.sleep(1)
                break
        print(screen)
        # pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", confidence=0.9)
        # pyautogui.click(x=pos1.x, y=pos1.y)
        time.sleep(1)
    while True:
        screen = check_screen()
        if screen['name'] == 'home':
            status = start_farm(stage=3, lvl="easy")
            if not status:
                pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/x-btn.png", confidence=0.9)
                pyautogui.click(x=pos1.x, y=pos1.y)
                time.sleep(1)
                break
        print(screen)
        # pos1 = pyautogui.locateCenterOnScreen("./resources/buttons/back-button.png", confidence=0.9)
        # pyautogui.click(x=pos1.x, y=pos1.y)
        time.sleep(1)
```

như trên mình cho bot chạy solo 3 map với config hero ở trên

# Bot hiện chỉ chạy được 1 account một máy cho cơ chế chiếm chuột và màn hình, a e làm muốn chạy nhiều account có thể sử dụng vmware or virtual box

# Code này mình mới test được trên Ubuntu, trên window a e tự quẩy
