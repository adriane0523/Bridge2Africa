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

import json
import queue

import threading

from  gtts import gTTS
from pygame import mixer

from tempfile import TemporaryFile


from parse_website import get_headers
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
NAV = ["", "headers", "links", "title", "body", "inputs"]

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
                CONTAINER = page_soup.find('body')
                    
            
        except:
            BROWSER_OPEN = False
           


def browser_nav():
    global CONTAINER
    global SPEAK
    global engine

    page_soup = soup(CONTAINER, "html.parser")
    print(CONTAINER)

    get_headers(page_soup)
    engine.stop()
    #print(CONTAINER)


def send_data(ser, first, second):
    arduino(ser, first)
    time.sleep(1)
    column_count = second
    ser.write(bytes([column_count]))    
    print (ser.readline()) # Read the newest output from the Arduino
    cache.append(first)

def clear_cache (ser):
    global cache
    
    column_count = 0
    for i in range(len(cache)):
        print("")
        arduino(ser, cache[i])
        arduino(ser, column_count)
        column_count = column_count + 1

    cache = []

def get_2s_complement(data):
    result = - data
    return (bin(result))


def voice():
    global TEMP_SPEAK
    global SPEAK
    
    TEMP_SPEAK = SPEAK
    engine.say(SPEAK)
    engine.runAndWait()

#arduino communication via serial
def arduino(ser, character):
   
    #ser.write(str.encode(character) )
    ser.write(chr(character).encode())
    print (ser.readline()) # Read the newest output from the Arduino
    
#read .json files
def read_json():
    
    with open('data.json',"r") as json_file:
        data = json.load(json_file)
        return data

    return None

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
    print("short cut pressed")
    result = ""


    #----------------------------------
    #open url connection and read html 
    uClient = urlopen((str)(driver.current_url))
    page_html = uClient.read()
    uClient.close()
    
    #activate html parse tool and parse main body of website
    page_soup = soup(page_html, "html.parser")
    container = page_soup.find('body')
    #---------------------------------- 
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
                send_data(ser, x["shift"], count)
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

    engine.stop()
    engine.say(NAV[NAV_ID])
    engine.runAndWait()

    if (NAV_ID == len(NAV) -1):
        NAV_ID = 0
    else:
        NAV_ID += 1    

#main function
if __name__ == "__main__":
    #----------------------------------
    #intialize window and UI
    window = Tk()
    window.title("Bridge2Africa with EPICS")
    window.geometry('350x200')
    lbl = Label(window, text="Program is running")
    lbl.grid(column=0, row=0)
    btn = Button(window, text="settings")
    btn.grid(column=1, row=0)
   
    #----------------------------------
    #start thread to track web browser
    t = threading.Thread(target =track_webbrowser)
    THREADS.append(t)

    #----------------------------------
    #intialize shortcut 
    shortcut1 = 'alt+o' #open browser
    shortcut2 = 'alt+v' #open screen reader
    shortcut3 = 'alt+m' #
    shortcut4 = 'alt+n'
   
    print('Hotkey set as:', shortcut1)

    keyboard.add_hotkey(shortcut1, on_triggered) #<-- attach the function to hot-key
    keyboard.add_hotkey(shortcut2, on_triggered_read) #<-- attach the function to hot-key
    keyboard.add_hotkey(shortcut3, navigation) #this is just a test shortcut
    keyboard.add_hotkey(shortcut4, browser_nav ) #this allows navigation on a web browser
    #----------------------------------
    
    for i in THREADS:
        t.start()
    

    print("Press ESC to stop.")

    #on_triggered_read(driver)
    window.mainloop()
    keyboard.wait("esc")
   

    

  