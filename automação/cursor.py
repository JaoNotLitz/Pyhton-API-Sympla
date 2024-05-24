import pyautogui
import time



time.sleep(3)
x, y = pyautogui.position()

print(f"A posição atual do cursor do mouse é ({x}, {y})")