#make a input menu
import screenshot_reddit
import os
import sys

subreddit = input("Enter a subreddit: ")
limit = int(input("Enter an amount of posts: (try around 70, as some may be deleted, ect (max 499))"))
over18 = input("Over 18? (y/n): (some content is nsfw, depending on the subreddit)")
date = input("Date to start search from? (DD/MM/YY) (if you start from the 25/12/20, you will get the amount of posts you typed since 25/12/20)")

if over18 == "y":
    over18 = True
else:
    over18 = False

screenshot_reddit.screenshot_website(subreddit,limit,over18)

