import pyautogui
from PIL import ImageGrab
import numpy as np
import time

BROWSER_TAB_1 = (179, 36)
DINOSAUR_AREA = (332, 604, 386, 658)
WHITE_PX_COUNT = 247
RESTART_BTN = (617, 586, 666, 624)
RESTART_BLACK_PX_COUNT = 5326
JUMPS = 0
INTERVAL = 0.07


def restart():
    restart_area = ImageGrab.grab(bbox=RESTART_BTN).convert("L")
    restart_color = restart_area.getcolors()
    restart_arr = np.array(restart_color).sum()
    return restart_arr


def cactus_ahead():
    grayscale_area = ImageGrab.grab(bbox=DINOSAUR_AREA).convert("L")
    colors = grayscale_area.getcolors()
    collision_arr = np.array(colors).sum(axis=0)[1]
    return collision_arr


def press_up():
    global JUMPS, INTERVAL

    if JUMPS < 7:
        time.sleep(0.024)
        pyautogui.press("up")
        JUMPS += 1
    else:
        pyautogui.press("up", interval=INTERVAL)
        pyautogui.press("down")
        JUMPS += 1
        INTERVAL *= 0.95


pyautogui.click(BROWSER_TAB_1)
pyautogui.press("up")

while True:
    if cactus_ahead() > WHITE_PX_COUNT:
        press_up()
    elif restart() == RESTART_BLACK_PX_COUNT:
        JUMPS = 0
        pyautogui.press("up")
