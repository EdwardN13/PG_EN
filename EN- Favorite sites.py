import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=lUhSxYUdm0E","https://www.youtube.com/watch?v=BnRhhCEHI0I","https://www.youtube.com/watch?v=17yYDtn8xOo"]

music = ["https://www.spotify.com/us/","https://www.pandora.com/"]

answer = pg.prompt(
"""
Which would you rather do?
a) Watch videos
b) Play music

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)
elif answer == "b":
    for i in music:
        webbrowser.open(i)
