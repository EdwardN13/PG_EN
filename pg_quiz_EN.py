import pyautogui as pg
import time
import webbrowser
points = 0

# Question 1

answer = pg.prompt(
"""
Which would you rather do?

a) Play a prank on a coworker
b) Host the Dundies
c) Run a fire safety drill
d) Organize a party in the office
e) Take an office trip to Gettysberg
"""

    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points+= 3
elif answer == "d":
    points+= 4
elif answer == "e":
    points += 5

# Question 2

answer = pg.prompt(
"""
What is your dream job?
a) Sports Marketing
b) Regional Manager (Living the dream)
c) Regional Manager (Not the assistant to the regional manager)
d) A Professional Cat Lady
e) Performer
"""

    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points+= 3
elif answer == "d":
    points+= 4
elif answer == "e":
    points += 5

# Question 3

answer = pg.prompt(
"""
What is your best punchline?
a) Bears. Beets. Battlestar Galatica
b) That's what she said
c) JIM! MICHEAL! 
d) If you try hard enough you can become a cat person.
e) Did you know that I graduated from CORNELL?
"""

    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points+= 3
elif answer == "d":
    points+= 4
elif answer == "e":
    points += 5

# Question 4

answer = pg.prompt(
"""
What is your biggest fear?
a) Working at a paper company for eternity
b) Dying alone
c) Losing Micheal 
d) Being demoted from head of the party planning commitee.
e) Losing your diploma from Cornell
"""


    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points+= 3
elif answer == "d":
    points+= 4
elif answer == "e":
    points += 5


# END OF SURVEY

pg.alert("You are...")

#Jim
if points < 7:
    pg.alert ("Jim Halpert")


#Micheal
elif points >=7 and points < 10:
    pg.alert ("Micheal G. Scott")

#Dwight
elif points >=10 and points < 13:
    pg.alert ("Dwight K. Shrute")
    webbrowser.open("http://3.bp.blogspot.com/-PFcTthywgu8/U2Bm40-XVuI/AAAAAAAADGY/HV3kRCgu6Fo/s1600/14+three+words.jpg")
    
#Angela
elif points >=14 and points < 18:
    pg.alert ("Angela Martin")

#Andy
elif points >=18 and points < 21:
     pg.alert("Andy Bernard")   
    



