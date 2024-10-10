import tkinter
import webbrowser
import time
import threading
import os
import sys

from tkinter import *

url = "https://www.youtube.com/watch?v=xvFZjo5PgG0"
timerIsRunning = False

def openUrl():
    webbrowser.open(url, new=0, autoraise=True)
    

def countdown(t, onStartCallback, onEndCallback, eachSecondCallback): 

    
    def delayCallback(t):
        onStartCallback()
        
        while t: 
            mins, secs = divmod(t, 60)
            eachSecondCallback('{:02d}:{:02d}'.format(mins, secs))
            time.sleep(1)
            t -= 1
            
        onEndCallback()
    
    thread = threading.Thread(target= lambda : delayCallback(t))
    thread.start()

def GUI():
    m = tkinter.Tk()
    m.title("😁")
    m.resizable(False, False)

    wDesc = Label(m, text="An app")
    wDesc.grid(row=0)
    
    wTime = Label(m, text="00:00")
    wTime.grid(row=2)

    wButton = Button(m, text="Click Me!", width=25, command = lambda : countdown(5, onTimerStart, onTimerEnd, lambda text : eachSecond(text)))
    wButton.grid(row=1)
    
    def onTimerStart():
        wButton.config(state="disabled")
        
    def eachSecond(text):
        wTime.config(text= text)
        
    def onTimerEnd():
        openUrl()
        wTime.config(text="Get Rickrolled!")
        wButton.config(state="active")

    m.mainloop()
GUI()
