import pyautogui as pg
import cv2
import numpy as np
import time


lower = np.array([107,75,80])
tolerance = np.array([1, 2, 2])

lower = target - tolerance
upper = target + tolerance


def find_pixel():
    screenshot = np.array(pg.screenshot())

    hsv = cv2.cvtColor(screenshot, cv2.COLOR_RGB2HSV)

    mask = cv2.inRange(hsv, lower, upper)

    # Find coordinates where mask == 255
    yp, xp = np.where(mask == 255)

    if len(xp) == 0:
        return None

    # Pick the middle match (more stable than first)
    index = len(xp) // 2

    xp = xp[index]
    yp = yp[index]

    # change to logical pixels
    x = xp // 2
    y = yp // 2 

    return x, y

def main():
    print("Starting bot...")
    time.sleep(2)

    while True:
        point = find_pixel()

        if point:
            print("Clicking:", point)
            pg.moveTo(point[0], point[1], duration=0.2)
            pg.click()
            #time.sleep(8)
        else:
            print("No matching pixel found")

        time.sleep(1)

if __name__ == "__main__":
    main()
