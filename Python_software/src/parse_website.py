from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup as soup
import re

def get_headers(container, nav_type):
    '''
    HTML parses all headers, page title, and paragraphs 
    accepts the HTML from the page, and current navigation the user is on
    returns array of text corresponding to the navigation type (paragraph, header, title)
    '''
    result = []
    

    if (nav_type == "headers"):
        for headlines in container.find_all(["h1", "h2", "h3", "h4", "h5" ]):
            result.append(headlines.get_text(strip=True))


    elif(nav_type == "title"):
        title = container.find_all("title")
        for i in title:
            result.append(i.get_text(strip=True))

    elif (nav_type == "paragraph"):
        temp = ""
        for div in container.find_all('p'):
            result.append(div.get_text(strip=True))


    elif (nav_type == "links"):
        for link in container.find_all('a', href=True):
            temp = link['href']
            if temp[0:5] == "http":
                result.append(link['href'])

    print(result)
    return result

def describe_hierarchy(container):
    '''
    HTML parses all headers, page title, and paragraphs 
    accepts the HTML from the page
    return length of titles, headers and paragraphs, respectively
    '''
    result = [0,0,0,0]
    title = []
    header = []
    paragraph = []
    links = []

    for headlines in container.find_all(["h1", "h2", "h3", "h4", "h5" ]):
        header.append(headlines.get_text(strip=True))

    for i in container.find_all("title"):
        title.append(i.get_text(strip=True))

    for div in container.find_all('p'):
        paragraph.append(div.get_text(strip=True))
  
    for link in container.find_all('a', href=True):
        temp = link['href']
        print(temp[0:4])
        if temp[0:4] == "http":
            links.append(link['href'])

    print(links)
    result[0] = len(title)
    result[1] = len(header)
    result[2] = len(paragraph)
    result[3] = len(links)

    print(result)

    return result