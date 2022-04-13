import promptlib
import os,sys

from time import sleep
from screenshot_reddit_posts  import  screenshot_website
from screenshot_twitter_tweets import screenshot_tweets
#to build run:  pyinstaller src\menu.py --onefile --name ScreenshotTool

prompter = promptlib.Files()


def get_reddit_posts(subreddit: str, num_posts: int, dir: str) -> str:
    print("Please do not close this or the chrome process.")
    return screenshot_website(subreddit,num_posts,dir)

    
def get_twitter_posts(search_terms:str, num_posts: int, dir: str) -> str:
    print("Please do not close this or the chrome process.")
    return screenshot_tweets(search_terms,num_posts,dir)


def menu():
    print("""
    Welcome to the screenshotter! You can choose to take screenshots of:
    1. Reddit
    2. Twitter
    3. Quit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        dir = str(prompter.dir())
        subreddit = input("Enter subreddit (dont write the r/): ")
        num_posts = int(input("Enter number of posts (recommened 75 posts, max is 499, the more the longer): "))
        print("Images saved in: ", get_reddit_posts(subreddit,num_posts,dir))
        print("Returning to menu...")
        menu()
    elif choice == "2":
        dir = str(prompter.dir())
        search_terms = input("Enter search terms (only use keywords): ")
        num_posts = int(input("Enter number of posts (not always accurate): "))
        print("Images saved in: ", get_twitter_posts(search_terms,num_posts,dir))
        print("Returning to menu...")
        menu()
    elif choice == "3":
        sys.exit()
    else:
        print("Invalid choice")
        menu()


print("""\n   _____  _             ___                    _     \n  / ____|| |           / _ \                  ( )    \n | |     | |__   _ __ | | | | _ __ ___   _   _|/ ___ \n | |     | '_ \ | '__|| | | || '_ ` _ \ | | | | / __|\n | |____ | | | || |   | |_| || | | | | || |_| | \__ \n  \_____||_| |_||_|    \___/ |_| |_| |_| \__, | |___/\n                                          __/ |      \n                                         |___/       """)
print("""\n   _____                                     _             _   \n  / ____|                                   | |           | |  \n | (___    ___  _ __  ___   ___  _ __   ___ | |__    ___  | |_ \n  \___ \  / __|| '__|/ _ \ / _ \| '_ \ / __|| '_ \  / _ \ | __|\n  ____) || (__ | |  |  __/|  __/| | | |\__ \| | | || (_) || |_ \n |_____/  \___||_|   \___| \___||_| |_||___/|_| |_| \___/  \__|\n                                                               \n                                                               """)
print("""\n  _______             _ \n |__   __|           | |\n    | |  ___    ___  | |\n    | | / _ \  / _ \ | |\n    | || (_) || (_) || |\n    |_| \___/  \___/ |_|\n                        \n                        """)
print("Please Wait...")
sleep(1)
os.system('cls')
menu()
