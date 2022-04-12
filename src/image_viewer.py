import os
from tkinter import *
from PIL import ImageTk, Image

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
    #button_exit = Button(root, text=" EXIT ", command= exit1).grid(row=1, column=4, pady=10)
    button_delete = Button(root, text=" delete image", command= delete).grid(row=1, column=1, pady=10)
    button_forward = Button(root, text=" >> ", command=lambda: forward(2)).grid(row=1, column=2)

    status=Label(root, text='Image '+ str(1) +' of '+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    root.mainloop()

