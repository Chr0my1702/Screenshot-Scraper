from io import BytesIO
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


import chromedriver_autoinstaller
import sys
import src.scrape_reddit as scrape_reddit
from PIL import Image
import json
from time import sleep

def screenshot_website(subreddit, limit):
    def take_screenshot_of_element(filename):
        screenshot_as_bytes = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]").screenshot_as_png
        with open(str(filename+'.png'), 'wb') as f:
            f.write(screenshot_as_bytes)
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    #options.add_argument('headless')
    options.add_argument('no-sandbox')
    options.add_argument("window-size=2000x2000")
    #options.add_argument("disable-gpu")
    options.add_argument("force-device-scale-factor=1")
    options.add_argument("enable-javascript")
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(-10000,0)
    posts = scrape_reddit.get_posts(subreddit=subreddit, limit=limit)
    
    driver.get("chrome://settings/")
    sleep(0.5)
    #driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.5);')
    for post in posts:
        driver.get(post[0])
        #driver.execute_script("document.body.style.zoom = '50%'")
        sleep(0.5)
        try: # for the accept button on the bottom of the page
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/section/div/section/section/form[2]/button').click()
        except: pass

        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/button').click()
            try: # accept the filter for the image
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/div[5]/div/a/div/button').click()
            except: pass
        except: pass

        #create folder for subreddit
        try:
            os.mkdir(subreddit)
        except: pass
        print(int(posts.index(post))+1, "of", len(posts))
        take_screenshot_of_element(filename=(subreddit+"/"+str(post[1])))


    driver.close()
    
    return subreddit

