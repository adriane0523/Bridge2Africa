#Nadia's code goes here
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
from webdriver_manager.chrome import ChromeDriverManager

import numpy as np


def find_accessibility_score(link):
    result = ""
    driver_ = webdriver.Chrome(ChromeDriverManager().install())
    try:

        driver_.minimize_window()
        wave_link = "https://wave.webaim.org/report#/"
        urls = []
        urls.append(link)

        i = link

        arr = np.zeros((6,), dtype=float)
        driver_.get(wave_link + i)

        time.sleep(10)

        page_html = driver_.page_source

        # activate html parse tool and parse main body of website
        page_soup = soup(page_html, "html.parser")
        sidebar = page_soup.find(id="sidebar_wrapper")
        tabs = sidebar.find(id="tabs")
        summary = tabs.find(id="summary")
        numbers = summary.find(id="numbers")

        error = numbers.find(id="error").find('span').get_text()
        arr[0] = error
        contrast = numbers.find(id="contrast").find('span').get_text()
        arr[1] = contrast
        alert = numbers.find(id="alert").find('span').get_text()
        arr[2] = alert
        feature = numbers.find(id="feature").find('span').get_text()
        arr[3] = feature
        structure = numbers.find(id="structure").find('span').get_text()
        arr[4] = structure
        aria = numbers.find(id="aria").find('span').get_text()
        arr[5] = aria

        print('')
        print('error:', error)
        print("contrast:", contrast)
        print("alert:", alert)
        print("feature:", feature)
        print("structure:", structure)
        print("aria:", aria)

        driver_.close()

        arr1 = np.zeros(6)
        arr1[0] = 1
        arr1[1] = 2
        arr1[2] = 3
        arr1[3] = 4
        arr1[4] = 5
        arr1[5] = 6

        arr[0] = (1 - arr[0]/500)
        arr[1] = (arr[1] / 5)
        arr[2] = (1 - arr[2] / 2000)
        arr[3] = (arr[3] / 100)
        arr[4] = (arr[4] / 500)
        if arr[5] == 304:
            arr[5] = (arr[5] / 500)
        else:
            arr[5] = (arr[5] / 50)

        mean = np.mean(arr)
        
        if mean >= .5:
            result = "This website is accessible"
            print('This website is accessible')
        else:
            result = "This website is not accessible"
            print('This website is not accessible')
    except:
        result = "Can not anaylze website"
        driver_.close()
        
    return result
