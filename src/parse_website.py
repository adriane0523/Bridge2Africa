from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup as soup
import re

def get_headers(container, nav_type):
    result = []
    

    if (nav_type == "headers"):
            
        for headlines in container.find_all("h3"):
            result.append(headlines.text.strip())

    elif (nav_type == "links"):

        for link in container.find_all('a', attrs={'href': re.compile("^http://")}):
            result.append( link.get('href') )


    elif(nav_type == "title"):
        title = container.find("title")
        for i in title:
            result.append(i)

    elif (nav_type == "body"):
        body = container.find("body")
        the_contents_of_body_without_body_tags = body.findChildren(recursive=False)
        for i in the_contents_of_body_without_body_tags:
            result.append(i.get_text())

    elif (nav_type == "paragraph"):
        temp = ""
        body = container.find("body")
        for div in body.find_all('div'):
            temp = temp + div.get_text()
        print(temp)
        result = sent_tokenize(temp)

    elif (nav_type == "input"):
        pass

    print (result)
    return result