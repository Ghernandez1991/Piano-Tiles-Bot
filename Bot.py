
# IMPORT DEPENDENCIES
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con


# https://www.agame.com/game/magic-piano-tiles

# FIND OUT CURRENT MOUSE POSITION
# pyautogui.position()
# FIND POSITION FOR LANE 1
#Point(x=570, y=508)
# FIND POSITION FOR LANE 2
#Point(x=686, y=508)
# FIND POSITION FOR LANE 3
#Point(x=795, y=508)
# FIND POSITION FOR LANE 4
#Point(x=895, y=508)


# rgb VALUE OF BLACK IS 0,0,0

time.sleep(2)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    # sometimes the click will not registered if you click too fast
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)


# use while loop to stop. if q is not pressed the bot will keep going
while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(570, 508)[0] == 0:
        click(570, 550)
    if pyautogui.pixel(686, 508)[0] == 0:
        click(686, 550)
    if pyautogui.pixel(795, 508)[0] == 0:
        click(795, 550)
    if pyautogui.pixel(895, 508)[0] == 0:
        click(895, 550)
