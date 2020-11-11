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

    shortcut_readBraille = braille+'+up arrow' 
    shortcut_activateArduino = misc+'+up arrow'
    shortcut_navigation= speak+'+right arrow' 
    shortcut_accessibility = speak+'+v'
    shortcut_hierarchy = speak+'+left arrow'
    shorctut_indexMinus = speak+'+down arrow'
    shortcut_indexPlus = speak+'+up arrow'
    shortcut_speak = speak + '+space'


 

 
    print('Hotkey set as:', shortcut_readBraille, "Braille Read")
    print('Hotkey set as:', shortcut_navigation, "NAV: Title, Paragraph, header")
    print('Hotkey set as:', shortcut_indexPlus, "page nav add")
    print('Hotkey set as:', shorctut_indexMinus, "page nav minus")
    print('Hotkey set as:', shortcut_speak, "Speak")
    print('Hotkey set as:', shortcut_hierarchy, "Describe Hierarchy")
    print('Hotkey set as:', shortcut_activateArduino, "Turn on Arduino")
    print('Hotkey set as:', shortcut_accessibility, "Accessibility Software")
    

    keyboard.add_hotkey(shortcut_readBraille, on_triggered_read) #braille read
    keyboard.add_hotkey(shortcut_navigation, navigation )  #title, headers, paragraph
    keyboard.add_hotkey(shortcut_indexPlus, page_navigation_add) #page index
    keyboard.add_hotkey(shorctut_indexMinus, page_navigation_minus)
    keyboard.add_hotkey(shortcut_activateArduino, intialize_arduino) #page index
    keyboard.add_hotkey(shortcut_accessibility, web_accessibility) #page index
    keyboard.add_hotkey(shortcut_speak, on_triggered_speak)  #speak
    keyboard.add_hotkey(shortcut_hierarchy, hierarchy)  #describe heiarchy
    #----------------------------------
    
    for i in THREADS:
        i.start()
        i.join(0)
    
    run_GUI() #Run UI that has all the settings

   

    

  