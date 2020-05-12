#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  display_main.py
#  Author: Fin Mead [Meadeor]
#  Desc: Aggregate display for display mirror
#  Last updated: 10/5/2020
#  ##############################
#DEV NOTES
#Display time/date / x
#BUttons / x
#Water consumption recording x x
#Calendar x x
#Temp monitoring x x
#Temp control x x

#reminders x x
###################

#  Imports
import RPi.GPIO as GPIO
import time
import tkinter
from tkinter import *
date = time.strftime('%b %d, %Y') 
Time = time.strftime('%l:%M%p')
window = Tk()

#Declaration
awake = False


#Setup
GPIO.setwarnings(False) # Ignore warning
GPIO.setmode(GPIO.BOARD) # Use phys pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 12 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 12 to be an input pin and set initial value to be pulled low (off)



        
def main():
    window.geometry('600x900')
    window.title("main")
    lbl = Label(window, text= date + Time,background = 'black', foreground = 'white', font=("Arial Bold", 25))
    lbl.grid(column=0, row=0)
    lbl.config(anchor=CENTER)
    lbl.pack()
    #lbl2 = Label(window, text= Time, background = 'black', foreground = 'white',font=("Arial Bold", 25))
    #lbl2.grid(column=0, row=1)
    #lbl2.config(anchor=CENTER)
    #lbl2.pack()
    window.configure(bg='black')
    window.mainloop()
    #tkinter.TK(configure(bg='black'))
    #print date
    #print time

def peripherals():
    if GPIO.input(10) == GPIO.LOW:
        print("[exit] was pushed!")
        time.sleep(0.25)
    if GPIO.input(12) == GPIO.LOW:
        print("[previous] was pushed!")
        time.sleep(0.25)
    if GPIO.input(16) == GPIO.LOW:
        print("[next] was pushed!")
        time.sleep(0.25)
    if GPIO.input(18) == GPIO.LOW:
        print("[select] was pushed!")
        time.sleep(0.25)
        if awake == False:
            main()

while True: # Run forever
    peripherals()
    main()
