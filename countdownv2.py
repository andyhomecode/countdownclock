#!/usr/bin/python

# Countdown Clock
# Andy Maxwell
# August 31, 2018

from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime


import socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

#print(get_ip_address())


try:
    ip_address = get_ip_address()
except:
    ip_address = "offline"


### ---- SETUP PARAMETERS
# list to hold all the items. 
events = []

# add the events to show here.
# 0 string is the label.
# 1 is the date in a string in mm/dd/yyyy 24:00 format
# 2, leave as "".  It will hold the StringVar() that we'll update every second
# idea: add a "color" option to override?

events.append(["P1", "09/17/2018 00:00", ""])
events.append(["P2", "11/1/2018 00:00", ""])
events.append(["P3", "02/1/2019 00:00", ""])
events.append(["Wave 1", "07/1/2019 00:00", ""])
events.append(["Wave 2", "07/1/2020 00:00", ""])


# https://wiki.tcl.tk/37701
BGCOLOR = "midnight blue"
FGCOLOR = "light grey"

# ----- Definitions of functions -----

def quit(*args):
    # let's blow this taco stand
    root.destroy()


def remaining_text(messagetext, endtext):
    # function to make a nice display of the remainig time
    # pass in the text like "Christmas" and "12/24/2018 00:00" and it'll show "Christmas in 125 days 6:32:05"

    # parse the text string date
    endTime = datetime.datetime.strptime(endtext, "%m/%d/%Y %H:%M")
    # Get the time remaining until the event
    remainder = endTime - datetime.datetime.now()
    # remove the microseconds part
    remainder = remainder - datetime.timedelta(microseconds=remainder.microseconds)
    # put it together
    return messagetext +" in " + str(remainder)
    

# this runs every second
def show_time():

    # loop through all the events and update the text for the labels
    for event in events:
        # remaining_text makes the "Chrisrtmas in 20 days" type text when passed label and text of deadline
        event[2].set(remaining_text(event[0], event[1]))

    # Trigger this function again after 1 second (1000 ms)
    root.after(1000, show_time)

## ----- END OF DEFINITION OF FUNCTIONS.  STARTUP CONTINUES HERE

# Use tkinter lib for showing the clock
# set it up.
root = Tk()
style = ttk.Style()
style.theme_use('classic') # Any style other than aqua. Fixed background color bug on Mac
root.attributes("-fullscreen", True)
root.configure(background=BGCOLOR)
root.bind("x", quit)


# this is the font for the main elements
fnt = font.Font(family='Helvetica', size=90, weight='bold')

# this is for the About This Thing
smallfnt = font.Font(family='Helvetica', size=12, weight='normal')


# run through the list of events and dates...
for event in events:
    # create a string variable to be updated in the show_time() function
    event[2] = StringVar()
    # now make a label and put it up
    w = ttk.Label(root, textvariable=event[2], font=fnt, foreground=FGCOLOR, background=BGCOLOR) # make the labels
    w.pack(pady=10) # and just use the pack layout.  this'll put them in a nice stack.


# put the About at the bottom and how to exit

quitText = StringVar()
quitText.set("by Andy Maxwell | press X to quit | " + ip_address)


lblQuit = ttk.Label(root, textvariable=quitText, font=smallfnt, foreground=FGCOLOR, background=BGCOLOR)
lblQuit.place(relx=0, rely=1, anchor=SW)


# okay.  We're all set.  Wait a second then run show_time to set the labels and in there keep looping.
root.after(1000, show_time)

# This makes the gui just look for events and show crap.  
root.mainloop()
