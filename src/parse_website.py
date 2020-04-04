
from bs4 import BeautifulSoup as soup

def get_headers(container):
    result = []
    
    for headlines in container.find_all("h3"):
        print(headlines.text.strip())
        result.append(headlines.text.strip())
    print (result)