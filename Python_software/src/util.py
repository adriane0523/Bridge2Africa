import json    

def read_json():
    '''
    read data.json files
    '''
    with open('data.json',"r+") as json_file:
        data = json.load(json_file)
        
        return data
    return None

def read_shortcut():
    '''
    read shortcuts.json files
    '''
    data = {}
    with open('shortcuts.json',"r+") as json_file:
        data = json.load(json_file)
     
    json_file.close()
    return data


def write_json(data, filename='shortcuts.json'): 
    with open(filename,'w+') as f: 
        json.dump(data, f, indent=4) 
    f.close()