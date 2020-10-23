from tkinter import *

#Dylan will work on this
#Goal to create UI to:

#input COM Port
#voice talking speed
#customize braille speed
#customize braille shortcuts
#saving the settings

#This UI should be storing its values into a JSON file within this folder
#The program may request to restart the program, so a prompt will be required
window = Tk()

def run_GUI():
    global window
    window.title("Bridge2Africa with EPICS")
    window.geometry('350x200')
    lbl = Label(window, text="Program is running")
    lbl.grid(column=0, row=1)
    settings = Button(window, text="settings", command = openSettings())
    settings.grid(column=1, row=2)
    exit_ = Button(window, text = "Exit", fg = 'red').grid(row = 0)
    window.mainloop()


def openSettings():
    global window 
    voiceSpeed = Label(window, text = "Adjust Voice Speed: ").grid(row = 1)
    voiceSpeedAdjust = Entry()
    voiceSpeedAdjust.grid(row = 1, column = 1)
    browser = Button(window, text = "Open Browser").grid(row = 2)#add a function that opens the browser
    screenRead = Button(window, text = "Start Screen Read").grid(row = 3) #add the function that starts screen read   
