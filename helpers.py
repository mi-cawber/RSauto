import numpy as np
import pyautogui as pg
import time
import cv2


def get_lower_upper(target: np.array) -> np.array:
    # HSV tolerance
    tolerance = np.array([1, 2, 2])

    # define upper, lower HSV values
    lower = target - tolerance
    upper = target + tolerance

    return lower, upper

def match_pixel(img, lower, upper):
    mask = cv2.inRange(img, lower, upper)

    # Find coordinates where mask == 255
    yp, xp = np.where(mask == 255)

    if len(xp) == 0:
        return None, None

    # Pick the middle match (more stable than first)
    index = len(xp) // 2

    xp = xp[index]
    yp = yp[index]

    # change to logical pixels
    x = xp // 2
    y = yp // 2 

    return x, y

def find_pixel(target):
    screenshot = np.array(pg.screenshot())

    hsv = cv2.cvtColor(screenshot, cv2.COLOR_RGB2HSV)

    lower, upper = get_lower_upper(target)

    x, y = match_pixel(hsv, lower, upper)

    return x, y

def click_point(point, rate=10):
        pg.moveTo(point[0], point[1], duration=0.5, tween=pg.easeInElastic)
        pg.click()
        time.sleep(rate)
