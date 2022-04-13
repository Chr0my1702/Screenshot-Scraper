import os,re, requests
from selenium import webdriver
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller
from time import sleep
from pathlib import Path

def get_posts(subreddit, limit):
    '''limit is the number of posts to be scraped, max to be 499'''
    def get_reddit(subreddit, limit):
        try:
            base_url = f'https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&size={limit}'
            request = requests.get(base_url, headers={'User-agent': 'yourbot'})
        except:
            print('An Error Occured')
        return request.json()

    def get_post_urls_and_titles(json_posts):
        posts = []
        for post in range(0, len(json_posts['data'])):
            x = json_posts['data'][post]['full_link']
            y = json_posts['data'][post]['title']
            # remove any special characters from the title
            y = re.sub('\W+', '', y)
            posts.append([x, y, subreddit])
        return posts

    r = get_post_urls_and_titles(get_reddit(subreddit, limit))

    return r

def screenshot_website(subreddit, limit, directory):
    def take_screenshot_of_element(filename):
        screenshot_as_bytes = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]").screenshot_as_png
        with open(str(filename+'.png'), 'wb') as f:
            f.write(screenshot_as_bytes)
            f.close()
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument('no-sandbox')
    options.add_argument("window-size=2000x2000")
    options.add_argument("force-device-scale-factor=1")
    options.add_argument("enable-javascript")
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(-10000,0)
    posts = get_posts(subreddit=subreddit, limit=limit)
    sleep(0.5)
    for post in posts:
        driver.get(post[0])
        sleep(0.5)
        try: # for the accept button on the bottom of the page
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/section/div/section/section/form[2]/button').click()
        except Exception: pass

        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/button').click()
            try: # accept the filter for the image
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/div[5]/div/a/div/button').click()
            except Exception: pass
        except Exception: pass

        print(int(posts.index(post))+1, "of", len(posts))
        take_screenshot_of_element(filename=(directory+'/'+post[1]))


    driver.close()
    
    return str(directory)