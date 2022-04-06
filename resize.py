import os 
from PIL import Image

def resize(im,new_width):
    width,height = im.size 
    ratio = height/width 
    new_height = int(ratio*new_width) 
    resized_image = im.resize((new_width, new_height)) 
    return resized_image 

files = os.listdir("images") 
extensions = ['jpg','jpeg','png','gif'] 

for file in files: 
    ext = file.split(".")[-1]
    if ext in extensions: 
        im = Image.open("images/" + file) 
        im_resized = resize(im,300) 
        filepath = f"images/{file}.png" 
        im_resized.save(filepath) 