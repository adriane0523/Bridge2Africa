from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint

def main():
    driver_ = webdriver.Chrome(executable_path ="chromedriver.exe") 


    wave_link  = "https://wave.webaim.org/report#/"
    urls = [
        "https://en.wikipedia.org/wiki/Arizona_State_University",
        "https://www.espn.com/",
        "https://www.asu.edu/"
    ]
    for i in urls:


        
        driver_.get(wave_link + i)
      
        time.sleep(10)
  
      
        page_html = driver_.page_source
     
   
        #activate html parse tool and parse main body of website
        page_soup = soup(page_html, "html.parser")
        sidebar = page_soup.find(id = "sidebar_wrapper")
        tabs = sidebar.find(id = "tabs")
        summary = tabs.find(id = "summary")
        numbers = summary.find(id = "numbers")
      
        error = numbers.find(id="error").find('span').get_text()
        contrast = numbers.find(id="contrast").find('span').get_text()
        alert = numbers.find(id="alert").find('span').get_text()
        feature = numbers.find(id="feature").find('span').get_text()
        structure = numbers.find(id="structure").find('span').get_text()
        aria =  numbers.find(id="aria").find('span').get_text()
        print('error:',error)
        print("contrast:",contrast)
        print("alert:", alert)
        print("feature:", feature)
        print("strucutre:", structure)
        print("aria:", aria) 
        driver_.close()
        driver_ = webdriver.Chrome(executable_path ="chromedriver.exe")          
        time.sleep(2)


if __name__ == "__main__":
    main()