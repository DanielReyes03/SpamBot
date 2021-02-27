import pyautogui as py
import time as t
import clipboard as c
from sys import platform

def startSpamming():
    imagePath = input('Escribe la direccion de la imagen del input en donde haremos spamm >> ')
    textToSpamm = input('Escribe el texto con el que quieres hacer SPAM >> ')
    c.copy(str(textToSpamm))
    print('Cambia hacia la ventana de donde haras spamm')
    t.sleep(5)
    cord = py.locateOnScreen(str(imagePath))
    py.click(cord)
    while True:
        if platform == "linux" or platform == "linux2":
            py.hotkey('ctrl', 'v')
            py.hotkey('enter')
        elif platform == "darwin":
            py.hotkey('command', 'v')
            py.hotkey('enter')
        elif platform == "win32":
            py.hotkey('ctrl', 'v')
            py.hotkey('enter')


startSpamming()