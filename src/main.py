from tkinter import *

import os
import time
import keyboard


import pyttsx3
import serial

from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import queue

import threading

from  gtts import gTTS
from pygame import mixer

from tempfile import TemporaryFile


from parse_website import get_headers
from util import *
from driver import *

import sys
#----------------------------------
#global variables
BROWSER_OPEN = False
driver = None 
#ser = serial.Serial('COM11', 9600)
ser = None
THREADS = []
CONTAINER = ""
SPEAK = ""
TEMP_SPEAK = ""
NAV_ID = 0
NAV = ["","headers", "links", "title", "body", "paragraph", "inputs"]
NAV_NODE = 0
CONTAINER_BRAILLE = ""

#----------------------------------
#intialize speech sythensizer
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+100)
#----------------------------------
cache = []

def track_webbrowser():
    global BROWSER_OPEN
    global CONTAINER
    global NAV_NODE
    current_website = None
    while(True):
        if (driver == None):
            BROWSER_OPEN = False
        try:

            if (driver.current_url !=  current_website or BROWSER_OPEN == True):
                current_website = driver.current_url

                
                #----------------------------------
                #open url connection and read html 
                uClient = urlopen((str)(current_website))
                page_html = uClient.read()
                uClient.close()
                
                #activate html parse tool and parse main body of website
                page_soup = soup(page_html, "html.parser")
                CONTAINER = page_soup
                NAV_NODE = 0
                    
            
        except:
            BROWSER_OPEN = False
           


def browser_nav():
    global CONTAINER
    global SPEAK
    global engine
    global NAV
    global NAV_ID
    global NAV_NODE
    global CONTAINER_BRAILLE
    #print(CONTAINER)
   
    

    print( NAV[NAV_ID])
    engine.stop()
    result = get_headers(CONTAINER, NAV[NAV_ID])

    engine.say(result[NAV_NODE])
    CONTAINER_BRAILLE = result[NAV_NODE]
    engine.runAndWait()


  

    if (NAV_NODE == len(result)-1):
        NAV_NODE = 0
    else:
        NAV_NODE += 1
    

  
    #print(CONTAINER)





#on shortcut trigger
#open chrome driver and go to google.com
def on_triggered(): 
    global test
    global driver
    global engine
    global BROWSER_OPEN

    print("short cut pressed")
    engine.say('Short Cut pressed. Opening new Webrowser')
    engine.runAndWait()
    driver_ = webdriver.Chrome(executable_path ="chromedriver.exe") 
    driver_.maximize_window()

    engine.say('Current website google.com')
    engine.runAndWait()
    driver_.get("https://www.google.com/")
    driver = driver_
    BROWSER_OPEN = True

    
#Start reading the information on the website and send it to the arduino
def on_triggered_read():
    #local variables/global variable references
    global ser
    global driver
    global CONTAINER_BRAILLE
    print("short cut pressed")
    result = ""

    engine.stop()
    #----------------------------------
    #open url connection and read html 
    uClient = urlopen((str)(driver.current_url))
    page_html = uClient.read()
    uClient.close()
    
    #activate html parse tool and parse main body of website
    page_soup = soup(page_html, "html.parser")
    container = page_soup.find('body')
    #---------------------------------- 
    comment_out  = '''
    custom = False
    engine.say('Custom passage read?    type y for yes or n for no')
    engine.runAndWait()
    print("Custom passage read?")
    print("type y or n")
    flag  = True
    while (flag):

        if keyboard.is_pressed('y'):
            flag = False
            custom = True
        if keyboard.is_pressed('n'):
            flag = False
            custom = False

    #----------------------------------
    #gets all string data from each div within a website

    engine.say('Adding passages to custom read.     type y to add or no to not add or q to quit')
    engine.runAndWait()
    for div in container.find_all('div'):

        if div.text != "":
            if (custom):
                print("ADD?: " + div.text)
                engine.say(div.text)
                engine.runAndWait()

                flag = True
                add = False
                while (flag):
                    if keyboard.is_pressed('y'):
                        flag = False
                        add = True
                    if keyboard.is_pressed('n'):
                        flag = False
                        add = False
                    if keyboard.is_pressed('q'):
                        break

                
                if (add):
                    result = result + (str)(div.text)
                time.sleep (1)
            else:    
                result = result + (str)(div.text)
    
    result = result.strip(' \n\t')
    '''
    result = CONTAINER_BRAILLE
    print(result)
    result = result.lower()
    data = read_json()
    #----------------------------------

    #goes to each letter references data.json and sends data arduino
    #pause, quit, go are shortcuts to use when translation is happening

    engine.say('translating to braille')
    engine.runAndWait()
    count = 0

    for i in result:
        print("\ncharacter",i)
        
        #send data
        for x in data["letters"]:
            
            if x["letter"] == i:
                print("CELL:",count)
                print (x["shift"])
                #send_data(ser, x["shift"], count)
                time.sleep(1)

                if (count == 9):
                    count = 0
                    clear_cache(ser)
                else:
                    count = count + 1

        #quit
        if keyboard.is_pressed('alt+q'):  
            print("quitting")
            break  # finishing the loop    

        #pause/unpaise
        if keyboard.is_pressed('alt+p'):  
            print('pausing')
            flag = True

            while(flag):
                if keyboard.is_pressed('alt+p'):  
                    print('unpause')
                    flag = False
           
        
#this is a test function for shortcut    
def navigation():
    global NAV_ID
    global NAV 
    global engine
    global NAV_NODE

    engine.stop()
   
    
    NAV_NODE = 0
    if (NAV_ID == len(NAV)-1):
        NAV_ID = 0
    else:
        NAV_ID += 1
        engine.say(NAV[NAV_ID])
        engine.runAndWait()    

def quit_program():
    global THREADS
    print("Quiting...")
    sys.exit(0)
    print("sleeping")
    time.sleep(5)

def openSettings() : 
    voiceSpeed = Label(window, text = "Adjust Voice Speed: ").grid(row = 1)
    voiceSpeedAdjust = Entry()
    voiceSpeedAdjust.grid(row = 1, column = 1)
    browser = Button(window, text = "Open Browser").grid(row = 2)#add a function that opens the browser
    screenRead = Button(window, text = "Start Screen Read").grid(row = 3) #add the function that starts screen read   

#main function
if __name__ == "__main__":
    #----------------------------------
    #intialize window and UI
    window = Tk()
    window.title("Bridge2Africa with EPICS")
    window.geometry('350x200')
    lbl = Label(window, text="Program is running")
    lbl.grid(column=0, row=1)
    settings = Button(window, text="settings", command = openSettings())
    settings.grid(column=1, row=2)
    exit_ = Button(window, text = "Exit", fg = 'red').grid(row = 0)


 
    #----------------------------------
    #start thread to track web browser
    t = threading.Thread(target =track_webbrowser, daemon= True)
    
    THREADS.append(t)

    #----------------------------------
    #intialize shortcut 
    shortcut1 = 'z+o' #open browser
    shortcut2 = 'z+v' #open screen reader
    shortcut3 = 'z+m' #
    shortcut4 = 'z+n'
    shortcut5 = 'z+q'
   
    print('Hotkey set as:', shortcut1)

    keyboard.add_hotkey(shortcut1, on_triggered) #<-- attach the function to hot-key
    keyboard.add_hotkey(shortcut2, on_triggered_read) #<-- attach the function to hot-key
    keyboard.add_hotkey(shortcut3, navigation) #this is just a test shortcut
    keyboard.add_hotkey(shortcut4, browser_nav ) #this allows navigation on a web browser
   
    #----------------------------------
    
    for i in THREADS:
        i.start()
        i.join(0)
      
    

    print("Press ESC to stop.")

    #on_triggered_read(driver)
    window.mainloop()
    keyboard.wait("esc")
   

    

  