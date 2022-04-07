import tkinter as tk
import tkinter.font as tkFont
from src.image_viewer  import image_viewer
import src.resize as resize
import src.screenshot_reddit_posts  as screenshot_reddit_posts
import os,sys
from tkinter import filedialog

def startup_window():
    root = tk.Tk()
    #setting title
    root.title("Chr0my's Screenshot Tool")

    def get_posts_button_command():
        print(subreddit_entry.get(),int(num_posts_entry.get()))
        dir = screenshot_reddit_posts.screenshot_website(subreddit_entry.get(),int(num_posts_entry.get()))
        resize.resize_keeping_aspect_ratio(dir,int(500),int(500),int(500))
        root.destroy()
        image_viewer(('resized_'+dir), dir)

    def load_folder_button_command():
        folder = filedialog.askdirectory()
        root.destroy()
        head_tail = os.path.split(folder)
        try:
            os.listdir(head_tail[0] + 'resized_' + head_tail[1])            
            image_viewer((head_tail[0] + 'resized_' + head_tail[1]),folder)
        except:
            resize.resize_keeping_aspect_ratio(head_tail[1],int(500),int(500),int(500))
            image_viewer(('resized_'+head_tail[1]),folder)

    #setting window size
    width=500
    height=350
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    welcome_text=tk.Label(root)
    welcome_text["cursor"] = "heart"
    ft = tkFont.Font(family='Times',size=15)
    welcome_text["font"] = ft
    welcome_text["fg"] = "#333333"
    welcome_text["justify"] = "center"
    welcome_text["text"] = "Welcome  to Chr0my's reddit scraper and discriminator\nPlease make a good video!"
    welcome_text["relief"] = "flat"
    welcome_text.place(x=10,y=4,width=500,height=40)

    #subreddit
    subreddit_text=tk.Label(root)
    ft = tkFont.Font(family='Times',size=18)
    subreddit_text["font"] = ft
    subreddit_text["fg"] = "#333333"
    subreddit_text["justify"] = "center"
    subreddit_text["text"] = "Enter a subreddit:"
    subreddit_text.place(x=0,y=70,width=250,height=40)

    subreddit_entry=tk.Entry(root)
    subreddit_entry["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=18)
    subreddit_entry["font"] = ft
    subreddit_entry["fg"] = "#333333"
    subreddit_entry["justify"] = "center"
    subreddit_entry.place(x=250,y=70,width=250,height=40)

    #amount of posts
    num_posts_text=tk.Label(root)
    ft = tkFont.Font(family='Times',size=18)
    num_posts_text["font"] = ft
    num_posts_text["fg"] = "#333333"
    num_posts_text["justify"] = "center"
    num_posts_text["text"] = "Enter amount of posts:"
    num_posts_text.place(x=0,y=130,width=250,height=40)

    num_posts_entry=tk.Entry(root)
    num_posts_entry["borderwidth"] = "3px"
    ft = tkFont.Font(family='Times',size=18)
    num_posts_entry["font"] = ft
    num_posts_entry["fg"] = "#333333"
    num_posts_entry["justify"] = "center"
    num_posts_entry.place(x=250,y=130,width=250,height=40)

    recommended_text=tk.Label(root)
    ft = tkFont.Font(family='Times',size=8)
    recommended_text["font"] = ft
    recommended_text["fg"] = "#333333"
    recommended_text["justify"] = "center"
    recommended_text["text"] = "Recommended = 75, Maxmium = 499, The more the longer it will take to load"
    recommended_text.place(x=0,y=180,width=500,height=30)

    #submit button
    get_posts_button=tk.Button(root)
    get_posts_button["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=18)
    get_posts_button["font"] = ft
    get_posts_button["fg"] = "#000000"
    get_posts_button["justify"] = "center"
    get_posts_button["text"] = "Get those posts!"
    get_posts_button.place(x=5,y=210,width=490,height=30)
    get_posts_button["command"] = get_posts_button_command

    #load folder
    load_folder_text=tk.Label(root)
    ft = tkFont.Font(family='Times',size=18)
    load_folder_text["font"] = ft
    load_folder_text["fg"] = "#333333"
    load_folder_text["justify"] = "center"
    load_folder_text["text"] = "Already got posts from a folder?"
    load_folder_text.place(x=0,y=265,width=500,height=30)

    load_folder_button=tk.Button(root)
    load_folder_button["bg"] = "#efefef"
    ft = tkFont.Font(family='Times',size=18)
    load_folder_button["font"] = ft
    load_folder_button["fg"] = "#000000"
    load_folder_button["justify"] = "center"
    load_folder_button["text"] = "Load from a folder"
    load_folder_button.place(x=5,y=300,width=490,height=30)
    load_folder_button["command"] = load_folder_button_command

    root.mainloop()
