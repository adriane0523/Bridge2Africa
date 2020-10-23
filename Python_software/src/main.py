import os
import threading

from GUI import *
from shortcuts import *

THREADS = []

#main function
if __name__ == "__main__":
    '''
    Main loop, this function deals with intialization, function threading, and shortcut threading
    '''

    intialize_speech() #intialize speech
    on_triggered() #opens webbrowser

    #start thread to track web browser
    t = threading.Thread(target = track_webbrowser, daemon= True)
    THREADS.append(t)

    #----------------------------------
    #shortcuts
    speak = 'z'
    braille = 'x'
    misc = 'c'

    shortcut1 = braille+'+up arrow' 
    shortcut6 = misc+'+up arrow'
    shortcut2 = speak+'+right arrow' 
    shortcut3 = speak+'+left arrow'
    shortcut4 = speak+'+down arrow' 
    shortcut5 = speak+'+up arrow'
    shortcut7 = speak + '+q'
    shortcut8 = speak + '+space'
 

 
    print('Hotkey set as:', shortcut1, "Braille Read")
    print('Hotkey set as:', shortcut2, "NAV: Title, Paragraph, header")
    print('Hotkey set as:', shortcut4, "page nav add")
    print('Hotkey set as:', shortcut5, "page nav minus")
    print('Hotkey set as:', shortcut8, "Speak")
    print('Hotkey set as:', shortcut5, "Describe Hierarchy")
    print('Hotkey set as:', shortcut6, "Turn on Arduino")
    print('Hotkey set as:', shortcut3, "Accessibility Software")
    

    keyboard.add_hotkey(shortcut1, on_triggered_read) #braille read
    keyboard.add_hotkey(shortcut2, navigation )  #title, headers, paragraph
    keyboard.add_hotkey(shortcut5, page_navigation_add) #page index
    keyboard.add_hotkey(shortcut4, page_navigation_minus)
    keyboard.add_hotkey(shortcut6, intialize_arduino) #page index
    keyboard.add_hotkey(shortcut7, web_accessibility) #page index
    keyboard.add_hotkey(shortcut8, on_triggered_speak)  #speak
    keyboard.add_hotkey(shortcut3, hierarchy)  #describe heiarchy
    #----------------------------------
    
    for i in THREADS:
        i.start()
        i.join(0)
    
    run_GUI() #Run UI that has all the settings

   

    

  