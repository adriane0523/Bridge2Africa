from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import pyttsx3
from pyttsx3.drivers import sapi5
import keyboard
import time
import serial
import sys


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from parse_website import*
from util import *
from driver import *
from accessibility import *


#----------------------------------
#global variables
INDEX = 1
TITLE = 0
HEADER = 0
P = 0
LINKS = 0
TITLE_INDEX = 0
HEADER_INDEX = 0
P_INDEX = 0
LINKS_INDEX = 0
CONTAINER = ""
NAV_ID = 0
NAV = ["headers", "title", "paragraph", "links"]
NAV_NODE = 0
CONTAINER_BRAILLE = ""
BROWSER_OPEN = False
driver = None 
ser = None
cache = []
engine = None
IS_BROWSER_OPEN=False
#----------------------------------

def buttons():
    global ser

    while True:
        # Serial read section
        print(ser.readline().decode())

def getBrowserOpen():
    global IS_BROWSER_OPEN

    return IS_BROWSER_OPEN

def close_driver():
    global driver
    global IS_BROWSER_OPEN
    if(IS_BROWSER_OPEN):
        driver.close()

def intialize_speech():
    '''
    intialize speech sythensizer
    '''
    global engine
    shortcut = read_shortcut()
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    rate_of_speech = (int)(shortcut["speed"]) + rate
    engine.setProperty('rate', rate_of_speech)


def intialize_arduino():
    '''
    intialize arduino
    '''
    global ser
    ser = serial.Serial('COM8', 9600)
    print("Success")


def track_webbrowser():
    '''
    Keep track of what webpage the use is currently on, if the page is switched then recheck page heirarchy, 
    reset indexes, and reset CONTAINER html with current page HTML
    '''

    global CONTAINER
    global NAV_NODE
    global TITLE
    global HEADER
    global P
    global LINKS
    global NAV_ID 

    global TITLE_INDEX
    global HEADER_INDEX
    global P_INDEX
    global LINKS_INDEX
    global IS_BROWSER_OPEN

    current_website = None

    while(True):
        try:
            windows = driver.window_handles
            if (len(windows) > 1):
                driver.switch_to.window(windows[1])
                driver.close()
                driver.switch_to.window(windoes[0])
            if (len(windows) <= 0):
                #print(IS_BROWSER_OPEN)
                IS_BROWSER_OPEN = False
            else:
                IS_BROWSER_OPEN = True

            #print("opened windows length: ", len(windows))
            if (driver.current_url !=  current_website):
                current_website = driver.current_url
                #----------------------------------
                #open url connection and read html 
                
                uClient = urlopen(Request((str)(current_website)))
                page_html = uClient.read()
                uClient.close()
                
                #activate html parse tool and parse main body of website
                page_soup = soup(page_html, "html.parser")
                CONTAINER = page_soup
                
                NAV_NODE = 0
                result = describe_hierarchy(CONTAINER)

                TITLE = result[0]
                HEADER = result[1]
                P = result[2]
                LINKS = result[3]
                                
                TITLE_INDEX = 0
                HEADER_INDEX = 0
                P_INDEX = 0
                LINKS_INDEX = 0
                time.sleep(1)
                NAV_ID = 0
                navigation()
    
        except:
            pass

def page_navigation_minus():
    '''
    decrement index on the coressponding navigation setting
    '''
    global NAV_ID
    global NAV 
    global engine
    global NAV_NODE

    global TITLE_INDEX 
    global HEADER_INDEX 
    global P_INDEX 
    global LINKS_INDEX

    engine.stop()

    if NAV_ID == 0:
       
        engine.say("Headers" + format(HEADER_INDEX - 1))
        engine.runAndWait()    
        
        if ( HEADER_INDEX == 0):
            HEADER_INDEX = 0
        else:
            HEADER_INDEX -= 1

    elif NAV_ID == 1:

        engine.say("Title" + format(TITLE_INDEX - 1))
        engine.runAndWait()    
        
        if ( TITLE_INDEX == 0):
            TITLE_INDEX = 0
     
        else:
            TITLE_INDEX -= 1
            
    elif NAV_ID == 2:
  
        engine.say("Paragraph" + format(P_INDEX - 1))
        engine.runAndWait()    
         
        if ( P_INDEX == 0 ):
            P_INDEX = 0
  
        else:
            P_INDEX -= 1

    elif NAV_ID == 3:
  
        engine.say("Links" + format(LINKS_INDEX - 1))
        engine.runAndWait()    
        
        if ( LINKS_INDEX  == 0 ):
            LINKS_INDEX = 0
        else:
            LINKS_INDEX -= 1


def page_navigation_add():
    '''
    Incrament index on the corresponding navgation setting
    '''

    global NAV_ID
    global NAV 
    global engine
    global NAV_NODE

    global TITLE_INDEX 
    global HEADER_INDEX 
    global P_INDEX 
    global LINKS_INDEX

    global CONTAINER
    global TITLE
    global HEADER
    global P
    global LINKS

    engine.stop()

    if NAV_ID == 0:
       
        engine.say("Headers" + format(HEADER_INDEX + 1))
        engine.runAndWait()    
        
        if ( (HEADER_INDEX + 1) == HEADER):
            HEADER_INDEX = 0
        else:
            HEADER_INDEX += 1

    elif NAV_ID == 1:
   
        engine.say("Title" + format(TITLE_INDEX + 1))
        engine.runAndWait()    
        
        if ( (TITLE_INDEX + 1) == TITLE):
            TITLE_INDEX = 0
        else:
            TITLE_INDEX += 1
            
    elif NAV_ID == 2:
  
        engine.say("Paragraph" + format(P_INDEX + 1))
        engine.runAndWait()    
        
        if ( (P_INDEX + 1) == P):
            P_INDEX = 0
        else:
            P_INDEX += 1
    elif NAV_ID == 3:
  
        engine.say("Links" + format(LINKS_INDEX + 1))
        engine.runAndWait()    
        
        if ( (LINKS_INDEX + 1) == LINKS):
            LINKS_INDEX = 0
        else:
            LINKS_INDEX += 1


def hierarchy():
    '''
    Count all headers, paragraphs, and titles then voice out the numbers
    '''
    global CONTAINER
    global TITLE
    global HEADER
    global P
    global LINKS

    engine.stop()
    result = describe_hierarchy(CONTAINER)

    engine.say("Current website " + driver.current_url)
    engine.runAndWait()
    time.sleep(0.2)
    prompt = "There are " + format(TITLE) + " Titles " + "There are " + format(HEADER) + " Headers "  
    prompt+=(" There are " + format(P) + " Paragraphs " + " There are " + format(LINKS) + " Links on this page")
   
    engine.say(prompt)
    engine.runAndWait()



def on_triggered_speak():
    '''
    Voice out the current navigation pointer depending on what index and navgation setting
    '''

    global CONTAINER
    global SPEAK
    global NAV
    global NAV_ID

    prompt = return_prompt()
    engine.stop()
    engine.say(prompt)
    engine.runAndWait()



def return_prompt():
    '''
    Gets navitgation pointer that is dependent on navigation index and navigation setting
    '''
    global NAV
    global NAV_ID
    global TITLE_INDEX 
    global HEADER_INDEX 
    global P_INDEX 
    global LINKS_INDEX
    global CONTAINER

    result = get_headers(CONTAINER, NAV[NAV_ID])
    prompt = ""
    if NAV_ID == 0:
        print(result[HEADER_INDEX]) 
        prompt = result[HEADER_INDEX]

    elif NAV_ID == 1:
        print(result[TITLE_INDEX]) 
        prompt = result[TITLE_INDEX]

    elif NAV_ID == 2:
        print(result[P_INDEX])
        prompt = result[P_INDEX]
    elif NAV_ID == 3:
        print(result[LINKS_INDEX])
        prompt = result[LINKS_INDEX]

    return prompt

def on_triggered(): 
    '''
    Intialize driver and open google
    '''
    global test
    global driver
    global engine
    global BROWSER_OPEN

    engine.say('Opening new Webrowser')
    engine.runAndWait()
    driver_ = webdriver.Chrome(ChromeDriverManager().install())
    driver_.maximize_window()

    engine.say('Current website google.com')
    engine.runAndWait()
    driver_.get("https://www.google.com/")
    driver = driver_
    BROWSER_OPEN = True

    
#Start reading the information on the website and send it to the arduino
def on_triggered_read():
    '''
    Start braille read
    '''
    global ser
    global driver
    global CONTAINER_BRAILLE
    global engine
    global cache

    result = return_prompt()
    result = result.lower()
    data = read_json()
    #----------------------------------
    engine.say('translating to braille')
    engine.runAndWait()
    webinfo_to_arduino( ser, engine, result, data, cache )


def navigation():
    '''
    iterate through the navigation settings
    '''
    global NAV_ID
    global NAV 
    global engine
    global NAV_NODE
    
    global TITLE_INDEX 
    global HEADER_INDEX 
    global P_INDEX 
    global LINKS_INDEX

    engine.stop()

    NAV_NODE = 0
    if (NAV_ID == len(NAV)-1):
        NAV_ID = 0
    else:
        NAV_ID += 1
    engine.say(NAV[NAV_ID])
    engine.runAndWait()

    if (TITLE_INDEX == 0):
        page_navigation_add()
    elif (HEADER_INDEX == 0):
        page_navigation_add()
    elif (P_INDEX == 0):
        page_navigation_add()
    elif (LINKS_INDEX == 0):
        page_navigation_add()

def web_accessibility():
    '''
    run accessibility software
    '''
    global NAV_ID
    global NAV
    global LINKS_INDEX
    global CONTAINER

    if (NAV[NAV_ID] == "links"):
        result = get_headers(CONTAINER, NAV[NAV_ID])
        link = result[LINKS_INDEX]
        score = find_accessibility_score(link)
        engine.say(score)
        engine.runAndWait()    
        
