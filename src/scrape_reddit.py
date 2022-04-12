import re
import json
import requests

print("omg this works")

def get_posts(subreddit: str, limit: int) -> list:
    '''limit is the number of posts to be scraped, max to be 499'''
    def get_reddit(subreddit: str, limit: int)_ dict:
        try:
            base_url = f'https://api.pushshift.io/reddit/search/submission/?subreddit={subreddit}&size={limit}'
            request = requests.get(base_url, headers={'User-agent': 'yourbot'})
        except Exception:
            print('An Error Occured')
        return request.json()

    def get_post_urls_and_titles(json_posts: dict) -> list:
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


