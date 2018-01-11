import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',.2)
pg.hotkey('winleft','up')
pg.typewrite('espn.com\n',.2)
time.sleep(6)
pg.moveTo(148, 179)
pg.click(148,179,1,)
pg.moveTo(549, 442)
pg.click(549,442)
time.sleep(3)
pg.hotkey('space')
pg.moveTo(602,408)
pg.click(602,408)
