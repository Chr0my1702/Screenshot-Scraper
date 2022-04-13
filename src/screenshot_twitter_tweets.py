import os
import chromedriver_autoinstaller

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep
from pathlib import Path


def get_tweets(searchText, limit):
    list_of_tweets = list()
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument('headless')
    options.add_argument('no-sandbox')
    options.add_argument("window-size=2000x2000")
    options.add_argument("force-device-scale-factor=1")
    options.add_argument("enable-javascript")
    driver = webdriver.Chrome(options=options)
    #driver.set_window_position(-10000,0)
    #posts = scrape_reddit.get_posts(subreddit=subreddit, limit=limit)
    #inbetween each word in searchText, add a %20
    searchText = searchText.replace(" ", "%20")
    driver.get("https://twitter.com/search?q="+searchText+"&src=typed_query")
    sleep(5)
    for i in range(0, round(limit/5)):
        driver.execute_script("""function getElementByXpath(path) {return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}getElementByXpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div").style = "";""")
        for t in range(1, len(driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div"))):
            element = driver.find_element(By.XPATH, """/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div["""+str(t)+"""]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a""")
            url = str(element.get_attribute("href"))
            username = driver.find_element(By.XPATH, """/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div["""+str(t)+"""]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/div/div[2]/div/a/div/div/span""")
            filename = username.text + "" + url.replace("https://twitter.com/", "").replace("/status/", "").replace("/", "")
            element.text
            if not url in list_of_tweets:
                list_of_tweets.append((url, filename))

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
    return list_of_tweets

def screenshot_tweets(searchText, limit, directory):
    def take_screenshot_of_element(filename):
        screenshot_as_bytes = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div[1]").screenshot_as_png
        with open(str(filename+'.png') , 'wb') as f:
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
    posts = get_tweets(searchText, limit)

    for post in posts:
        driver.get(post[0])

        sleep(2)
        try: # for the accept button on the bottom of the page
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div').click()

        except: pass
        try: # to delete the login and signup bottom of the page
            driver.execute_script("""function getElementByXpath(path) {return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}getElementByXpath("/html/body/div[1]/div/div/div[1]/div/div[1]").remove();""")
        except: pass

        print(int(posts.index(post))+1, "of", len(posts))

        take_screenshot_of_element(filename=directory+'/'+post[1])

    driver.close()

    return str(directory)