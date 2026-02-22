import pyautogui as pg
import time

print("Move mouse to TOP-LEFT of game window")
time.sleep(5)
top_left = pg.position()
print("Top-left:", top_left)

print("Move mouse to BOTTOM-RIGHT of game window")
time.sleep(5)
bottom_right = pg.position()
print("Bottom-right:", bottom_right)

width = bottom_right.x - top_left.x
height = bottom_right.y - top_left.y

print("GAME_REGION =", (top_left.x, top_left.y, width, height))
