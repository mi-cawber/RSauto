import pyautogui as pg
import helpers as h
import utils as u
import time

def fish():
    while True:
        point = h.find_pixel(u.raw_salmon)

        # check for valid point
        if point[0] != None:
            h.click_point(point, rate=90)
        else:
            print("No matching pixel found")

        time.sleep(1)

def drop_inv():
    while True:
        point = h.find_pixel(u.raw_trout)

        # check for valid point
        if point[0] != None:
            pg.keyDown('shift')
            h.click_point(point, rate=1)
            pg.keyUp('shift')
        else:
            print("No matching pixel found")

        time.sleep(1)

