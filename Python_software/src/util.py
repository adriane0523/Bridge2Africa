import json    

def read_json():
    '''
    read .json files
    '''
    with open('data.json',"r") as json_file:
        data = json.load(json_file)
        return data

    return None