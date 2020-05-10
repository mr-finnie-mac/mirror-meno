#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  display_main.py
#  Author: Fin Mead [Meadeor]
#  Desc: Aggregate display for display mirror
#  Last updated: 10/5/2020
#  

#  Imports
import RPi.GPIO as GPIO
import time
import tkinter
from tkinter import *
date = time.strftime('%b %d, %Y') 
Time = time.strftime('%l:%M%p')
window = Tk()

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 12 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 12 to be an input pin and set initial value to be pulled low (off)



        
def main():
    window.geometry('1440x720')
    window.title("main")
    lbl = Label(window, text= date + Time, font=("Arial Bold", 50))
    lbl.grid(column=0, row=0)
    window.mainloop()
    #print date
    #print time

while True: # Run forever
    if GPIO.input(10) == GPIO.LOW:
        print("Button 0 was pushed!")
        #main()
        time.sleep(0.5)
    if GPIO.input(12) == GPIO.LOW:
        print("Button 1 was pushed!")
        #main()
        time.sleep(0.5)
    if GPIO.input(16) == GPIO.LOW:
        print("Button 2 was pushed!")
        #main()
        time.sleep(0.5)
    if GPIO.input(18) == GPIO.LOW:
        print("Button 3 was pushed!")
        #main()
        time.sleep(0.5)
