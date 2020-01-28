from tkinter import *

import os
import time
import keyboard


import pyttsx3
import serial
import speech_recognition as sr
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

import speech_recognition as sr

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import json




#----------------------------------
#global variables
driver = None 
ser = serial.Serial('COM5', 9600)
#----------------------------------


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
def on_triggered(): #define your function to be executed on hot-key press
    global test
    global driver

    #
    print("short cut pressed")
    driver_ = webdriver.Chrome(executable_path ="chromedriver.exe") 
    driver_.maximize_window()
    time.sleep(1)
    driver_.get("https://www.google.com/")
    driver = driver_

    

def on_triggered_read():
    #local variables
    global ser
    global driver
    print("short cut pressed")
    result = ""


    #----------------------------------
    uClient = urlopen((str)(driver.current_url))
    page_html = uClient.read()
    uClient.close()
    #----------------------------------

    #----------------------------------
    page_soup = soup(page_html, "html.parser")
    container = page_soup.find('body')
    #---------------------------------- 
    

    #----------------------------------
    #gets all string data from each div within a website
    for div in container.find_all('div'):
        result = result + (str)(div.text)

    result = result.strip(' \n\t')
    print(result)
    result.lower()
    data = read_json()
    #----------------------------------

    #goes to each letter references data.json and sends data arduino
    #pause, quit, go are shortcuts to use when translation is happening
    for i in result:
        print("\ncharacter",i)
        
        
        for x in data["letters"]:
            
            if x["letter"] == i:
                print("data:",x["shift"])
                arduino(ser, x["shift"])
                time.sleep(2)

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
def test():
    print("test")
    

    

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

    #----------------------------------
    #intialize speech sythensizer
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate+150)
    #----------------------------------
   
    #----------------------------------
    #intialize shortcut s
    text_to_print='default_predefined_text'
    shortcut1 = 'alt+o' #define your hot-key
    shortcut2 = 'alt+v'
    shortcut3 = 'alt+m'
    print('Hotkey set as:', shortcut1)

    keyboard.add_hotkey(shortcut1, on_triggered) #<-- attach the function to hot-key
    keyboard.add_hotkey(shortcut2, on_triggered_read) #<-- attach the function to hot-key
    keyboard.add_hotkey(shortcut3, test) #this is just a test shortcut
    #----------------------------------
    

    print("Press ESC to stop.")

    #on_triggered_read(driver)
    window.mainloop()
    keyboard.wait("esc")
   

    

  