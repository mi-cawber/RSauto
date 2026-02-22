import pyautogui as pg
import cv2
import numpy as np

while True:
    x, y = pg.position()
    screenshot = np.array(pg.screenshot())
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_RGB2HSV)

    # account for logical vs. physical pixels
    x = x * 2
    y = y * 2

    print(hsv[y, x])
