import time

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

#arduino communication via serial
def arduino(ser, character):
   
    #ser.write(str.encode(character) )
    ser.write(chr(character).encode())
    print (ser.readline()) # Read the newest output from the Arduino