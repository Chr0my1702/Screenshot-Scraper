import tkinter as tk # this is in python 3.4. For python 2.x import Tkinter
from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter import filedialog


class EditorWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.canvas = tk.Canvas(self, width=512, height=512, cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<MouseWheel>", self.do_zoom)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.rect = None

        self.start_x = None
        self.start_y = None
        self.open_image_button = Button(self.canvas, width=20, text='OPEN IMAGE', command=self.open_image)
        self.open_image_button.pack(pady=(10,5))

    def do_zoom(self, event):
        factor = 2 ** event.delta
        self.canvas.scale(self.canvas_image,0 , 0, factor, factor)
        #self._draw_image()
    def open_image(self):
        self.imagepath = filedialog.askopenfilename()
        self._draw_image(self.imagepath)
        #global image
        #global image_for_mask_multiplication
        #if path:
         #   image = Image.open(path)
          #  image_for_mask_multiplication = Image.open(path)
           # image = image.resize((500, 490), Image.ANTIALIAS)
            #image_for_mask_multiplication = image_for_mask_multiplication.resize((500, 490), Image.ANTIALIAS)
            #image = ImageTk.PhotoImage(image)
            #image_area.create_image(0, 0, image=image, anchor='nw')

    def _draw_image(self, imagepath):
        self.im = PIL.Image.open(imagepath)
        self.tk_im = ImageTk.PhotoImage(self.im)
        self.canvas_image = self.canvas.create_image(0,0,anchor="nw",image=self.tk_im, tag='image')



    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = event.x
        self.start_y = event.y

        # create rectangle if not yet exist
        #if not self.rect:
        self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, fill=None, width=10)

    def on_move_press(self, event):
        curX, curY = (event.x, event.y)

        # expand rectangle as you drag the mouse
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)



    def on_button_release(self, event):
        pass

if __name__ == "__main__":
    app = EditorWindow()
    app.mainloop()