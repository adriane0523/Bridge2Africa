import os
import threading
import sys

from GUI import *
from shortcuts import *


THREADS = []

#main function
if __name__ == "__main__":
    '''
    Main loop, this function deals with intialization, function threading, and shortcut threading
    '''
    intialize_arduino()
    intialize_speech() #intialize speech
    on_triggered() #opens webbrowser

    #start thread to track web browser
    t = threading.Thread(target = track_webbrowser, daemon= True)
    THREADS.append(t)

    t = threading.Thread(target = buttons, daemon= True)
    THREADS.append(t)

    #----------------------------------
    #shortcuts
    shortcut = read_shortcut()
    shortcut_readBraille = shortcut["readBraille"]
    shortcut_activateArduino = shortcut["activateArduino"]
    shortcut_navigation= shortcut["navigation"]
    shortcut_accessibility = shortcut["accessibility"]
    shortcut_hierarchy = shortcut["hierarchy"]
    shorctut_indexMinus = shortcut["indexMinus"]
    shortcut_indexPlus =shortcut["indexPlus"]
    shortcut_speak = shortcut["speak"]
    #shortcut_index_search = shortcut["indexSearch"]

    keyboard.add_hotkey(shortcut_readBraille, on_triggered_read) #braille read
    keyboard.add_hotkey(shortcut_navigation, navigation )  #title, headers, paragraph
    keyboard.add_hotkey(shortcut_indexPlus, page_navigation_add) #page index
    keyboard.add_hotkey(shorctut_indexMinus, page_navigation_minus)
    keyboard.add_hotkey(shortcut_activateArduino, intialize_arduino) #page index
    keyboard.add_hotkey(shortcut_accessibility, web_accessibility) #page index
    keyboard.add_hotkey(shortcut_speak, on_triggered_speak)  #speak
    keyboard.add_hotkey(shortcut_hierarchy, hierarchy)  #describe heiarchy
    #keyboard.add_hotkey(shortcut_index_search, search_indexing)  #describe heiarchy
    #----------------------------------
    
    for i in THREADS:
        i.start()
        i.join(0)
    

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_()) 
    close_driver()

    

  