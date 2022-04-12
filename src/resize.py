import os, pathlib
from PIL import Image
from pathlib import Path


def resize_via_width(im,new_width):
    width,height = im.size 
    ratio = height/width 
    new_height = int(ratio*new_width) 
    resized_image = im.resize((new_width, new_height)) 
    return resized_image 
#instead of basing the new aspect ratio on the width, which is the code above, we base it on the height
#basically, we are making the image taller, and then we are making it wider
def resize_via_hieght(im,new_height, limit_width,limit_height):
    width,height = im.size 
    ratio = width/height 
    new_width = int(ratio*new_height) 
    resized_image = im.resize((new_width, new_height)) 
    width,height = resized_image.size
    #if the image is too wide, we resize it again
    if width > limit_width:
        resized_image = resize_via_width(resized_image,limit_width)
    #if the image is too tall, we resize it again
    if height > limit_height:
        resized_image = resize_via_hieght(resized_image,limit_height, limit_width, limit_height)
    return resized_image


def resize_keeping_aspect_ratio(normal_size_image_foldername, height, limit_width, limit_height):
    #
    resizedfilepath = str(os.path.split(normal_size_image_foldername)[0] + '\\resized_' + os.path.split(normal_size_image_foldername)[1])
    files = os.listdir(normal_size_image_foldername)
    extensions = ['jpg','jpeg','png','gif'] 
    try:
        os.mkdir(f"{resizedfilepath}")
    except:
        #clear the folder
        for file in os.listdir(f"{resizedfilepath}"):
            os.remove(f"{resizedfilepath}/" + file)
    for file in files: 
        ext = file.split(".")[-1]
        if ext in extensions: 
            im = Image.open(normal_size_image_foldername + "/" + file) 
            im_resized = resize_via_hieght(im,height, limit_width, limit_height) 
            filepath = f"{resizedfilepath}/{file}" 
            im_resized.save(filepath)
        else:
            print(f"{file} is not an image (."+ext+")")

    return f"{resizedfilepath}"

