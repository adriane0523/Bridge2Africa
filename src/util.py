import json    


#read .json files
def read_json():
    
    with open('data.json',"r") as json_file:
        data = json.load(json_file)
        return data

    return None