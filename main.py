import pyautogui as py
import time as t

t.sleep(3)
cord = py.locateOnScreen('/Users/jose/Desktop/2.png')
py.click(cord)
while True:
    py.hotkey('command', 'v')
    py.hotkey('enter')