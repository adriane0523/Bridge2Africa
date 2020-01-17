from tkinter import *

import os
import time


import pyttsx3
import serial
import speech_recognition as sr
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import json


def arduino(ser, character):
    #ser.write(str.encode(character) )
    ser.write(chr(character).encode())
    print (ser.readline()) # Read the newest output from the Arduino
    
def read_json():
    
    with open('data.json',"r") as json_file:
        data = json.load(json_file)
        return data

    return None

if __name__ == "__main__":
    window = Tk()
    window.title("Bridge2Africa with EPICS")
    window.geometry('350x200')
    lbl = Label(window, text="Program is running")
    lbl.grid(column=0, row=0)
    btn = Button(window, text="settings")
    btn.grid(column=1, row=0)


    user_input = ""

    driver = webdriver.Chrome(executable_path ="chromedriver.exe") 
  

    driver.maximize_window()
    while(user_input != "x"):
        user_input = input(">")


        if (user_input == "o"):
            driver.get("https://www.google.com/")

        elif(user_input == "v"):
            uClient = urlopen((str)(driver.current_url))
            page_html = uClient.read()
            uClient.close()

            

            page_soup = soup(page_html, "html.parser")
            container = page_soup.find('body')
            
            result = ""
            
            for div in container.find_all('div'):
                result = result + (str)(div.text)




            flag = True
            start = 0
            end = 3
            result = result.strip(' \n\t')
            print(result)

            ser = serial.Serial('COM4', 9600)
            result.lower()
            data = read_json()
            for i in result:
                print(i)
               
               
                for x in data["letters"]:
            
                    if x["letter"] == i:
                        print(x["shift"])
                        arduino(ser, x["shift"])
                        
                        time.sleep(5)
            



        elif(user_input == "l"):
            pass
        


    window.mainloop()

  