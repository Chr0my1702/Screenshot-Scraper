from logging import root
import os
from tkinter import *
from PIL import ImageTk, Image
from numpy import delete
from tkinter import filedialog
import resize 
import screenshot_reddit

def start_page():
    def open_file_explorer(event=None):
        folder = filedialog.askdirectory()
        window.destroy()
        image_viewer(('resized_'+folder),folder)  

    def enter_new_video():
        print(subreddit.get(),int(posts.get()))
        dir = screenshot_reddit.screenshot_website(subreddit.get(),int(posts.get()))
        resize.resize_keeping_aspect_ratio(dir,int(500),int(500),int(500))
        window.destroy()
        image_viewer(('resized_'+dir), dir)
           
    
    window = Tk()
    window.title("Chr0my's Image Viewer")
    window.geometry('500x200')
    lbl = Label(window, text="Welcome, make a good video!")
    lbl.grid(column=1, row=0)

    
    subreddittext = Label(window, text="Make a new video, Enter a subreddit:")
    subreddittext.grid(column=1, row=1)
    subreddit = Entry(window,width=10)
    subreddit.grid(column=2, row=1)

    poststext = Label(window, text="Make a new video, Enter how many posts you want, rec=75 max=499:")
    poststext.grid(column=1, row=2)
    posts = Entry(window,width=10)
    posts.grid(column=3, row=2)


    newbtn = Button(window, text="Get those posts!", command=enter_new_video)
    newbtn.grid(column=1, row=5)


    btn = Button(window, text="Restore from existing folder", command=open_file_explorer)
    btn.grid(column=1, row=8)

    window.mainloop()


def image_viewer(resized_dir, real_dir):
    root = Tk()
    root.title('Image Viewer')

    
#add all image in list
    image_list = []

    for i in os.listdir(resized_dir):
        try:
            image_list.append(ImageTk.PhotoImage(Image.open(f"{resized_dir}/{i}")))
        except Exception as e:
            print(e)
            pass
# List of the images so that we traverse the list


#making lapel for image
    global my_label
    my_label = Label(image= image_list[0],)
    my_label.grid(row=0, column=0, columnspan=3)
    #set button on the root screen


    

    def forward(image_number):
        global my_label
        global button_forward
        global button_back

        my_label.grid_forget()
        my_label = Label(image= image_list[image_number-1])
        button_forward = Button(root, text=" >> ", command= lambda:forward(image_number+1))
        button_back = Button(root, text=" << ", command= lambda : back(image_number-1))

        if image_number == len(image_list):
            button_forward = Button(root, text=" >> ", state=DISABLED)

        button_forward.grid(row=1, column=2)
        button_back.grid(row=1, column=0)
        my_label.grid(row=0, column=0, columnspan=3)

    # Update Status bar
        status=Label(root, text='Image '+ str(image_number) +' of '+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)
        global image_num
        image_num = image_number

    def back(image_number):
        global my_label
        global button_forward
        global button_back
        my_label.grid_forget()
        my_label=Label(image=image_list[image_number-1])
        button_forward=Button(root, text=" >> ", command=lambda:forward(image_number+1))
        button_back=Button(root, text=" << ", command=lambda:back(image_number-1))

        if image_number == 1:
            button_back=Button(root, text=" << ", state=DISABLED)

        button_forward.grid(row=1, column=2)
        button_back.grid(row=1, column=0)
        my_label.grid(row=0, column=0, columnspan=3)

    # Update Status bar
        status=Label(root, text='Image '+ str(image_number) +' of '+str(len(image_list)), bd=1, relief=SUNKEN,    anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)
        global image_num
        image_num = image_number

    def exit1():
        exit()

    def delete():
        global my_label
        global button_forward
        global button_back
        global image_num
        image_num -= 1
        image_number = image_num
        my_label.grid_forget()
        my_label = Label(image= image_list[image_number-1])
        button_forward = Button(root, text=" >> ", command= lambda:forward(image_number+1))
        button_back = Button(root, text=" << ", command= lambda : back(image_number-1))


        button_forward.grid(row=1, column=2)
        button_back.grid(row=1, column=0)
        my_label.grid(row=0, column=0, columnspan=3)

    # Update Status bar
        status=Label(root, text='Image '+ str(image_number) +' of '+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    #delete current image from directory and list
        os.remove(f"{real_dir}/{os.listdir(real_dir)[image_number]}")
        os.remove(f"{resized_dir}/{os.listdir(resized_dir)[image_number]}")
        image_list.remove(image_list[image_number])
        button_forward.invoke()
    
    button_back = Button(root, text=" << ",  command=back, state=DISABLED).grid(row=1, column=0)
    button_exit = Button(root, text=" EXIT ", command= exit1).grid(row=1, column=4, pady=10)
    button_exit = Button(root, text=" delete image", command= delete).grid(row=1, column=1, pady=10)
    button_forward = Button(root, text=" >> ", command=lambda: forward(2)).grid(row=1, column=2)

    status=Label(root, text='Image '+ str(1) +' of '+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    root.mainloop()


start_page()