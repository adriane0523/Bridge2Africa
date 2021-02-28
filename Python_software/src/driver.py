import time
import keyboard


def send_data(ser, first, second,cache):
    '''
    Sends data from the website to the Arduino microcontroller
    accepts serial library, letter in decimal, column index, and cache array
    '''

    arduino(ser, first)
    time.sleep(1)
    column_count = second
    ser.write(bytes([column_count])) #sends number   
    print (ser.readline()) # Read the newest output from the Arduino
    cache.append(first)

def clear_cache (ser, cache):
    '''
    Clears letter cache
    accepts serial library and cache array
    '''
    
    column_count = 0
    for i in range(len(cache)):
        print("")
        arduino(ser, cache[i])
        arduino(ser, column_count)
        column_count = column_count + 1

    cache = []

def arduino(ser, character):
    '''
    Encodes character and sends it to the arduino, and reads any inputs from the arduino
    accepts serial library and letter/character (not number)
    '''
    #ser.write(str.encode(character) )
    ser.write(chr(character).encode())
    print (ser.readline()) # Read the newest output from the Arduino

def webinfo_to_arduino(ser, engine, text, data, cache):
    '''
    Goes to each letter references data.json and sends data to arduino,
    '''
    count = 0
    for i in text:
        print("\ncharacter",i)

        for x in data["letters"]:

            if x["letter"] == i:
                print("CELL:",count)
                print (x["shift"])

                if ser != None:
                    send_data(ser, x["shift"], count, cache)
                time.sleep(1)

                if (count == 9):
                    flag =True
                    print("Press x + right arrow to contiue")
         
                    while flag:
                        if keyboard.is_pressed('x+right arrow'):
                            count = 0
                            clear_cache(ser, cache)
                            flag = False
                else:
                    count = count + 1

        #quit
        if keyboard.is_pressed('x+down arrow'):  
            engine.say('quitting')
            engine.runAndWait()
            print("quitting")
            break  
