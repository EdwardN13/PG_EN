import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak ("What is your name")
answer = pg.prompt ("Enter in your name")

speak.Speak("Hello " + answer + "." + "Nice to meet you.")

speak.Speak("What is your favorite color?")
color = pg.prompt("Enter in your favorite color.")

if color == "Blue":
    speak.Speak("Liking the color blue brings bad luck.")
            

elif color == "Red":
    speak.Speak ("Red is the color of the Soviet Union, you are a communist, you will be terminated")

else:
    speak.speak("I don't like colors, I am colorblind hahahaha.")

speak.Speak("What is your favorite football team")
team = pg.prompt("Enter in your favorite football team?")

if team == "Baltimore Ravens":
    speak.Speak("Welcome to Ravens Nation, you are a good person.")

elif team == "Pittsburg Steelers":
    speak.Speak("Big Ben is far less superior than Joe Flacco.")

else:
    speak.Speak("I have lost all respect for you as a person.")

speak.Speak("What video would you like to watch?")
video = pg.prompt("Enter video here")
wb.open("https://www.youtube.com/results?search_query=" + video)

speak.Speak("What would you like to google search?")
search = pg.prompt("Enter google search here")
wb.open("https://www.google.com/search?q=" + search)
    
