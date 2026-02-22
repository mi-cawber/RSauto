import pyautogui as pg
import cv2
import numpy as np

while True:
    x, y = pg.position()
    screenshot = pg.screenshot()
    rgb = np.array(screenshot)

    # account for logical vs. physical pixels
    x = x * 2
    y = y * 2

    print(rgb[y, x])
