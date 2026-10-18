"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     TP1 Team 1
    Team ID:        SC1 - 05
    Author:         Edison Zheng, zhen1058@purdue.edu
    Date:           10/15/2026

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import numpy as np
import math as m
from PIL import Image,ImageOps
import matplotlib.pyplot as plt


#Reused functions to load images
def load_img(path):
    return np.array(Image.open(path))
def resize_image(original_image_array, new_size):
    # Convert the NumPy array to a Pillow image
    img = Image.fromarray(original_image_array)
    # Resize with bilinear interpolation; new_size is (width, height)
    resized = img.resize(new_size, Image.BILINEAR)
    return np.array(resized)
def pad_image(resized_img_array, target_size):
    # Convert the NumPy array to a Pillow image
    img = Image.fromarray(resized_img_array)
    # Center the image on a black canvas of target_size (width, height)
    padded = ImageOps.pad(img, target_size)
    return np.array(padded)
def rgb_to_hsv(R,G,B):
    r = R/255.0
    g = G/255.0
    b = B/255.0
    #Calculate intermediate values
    c_max = max(r,g,b)
    c_min = min(r,g,b)
    diff = c_max - c_min
    #Calculate values
    v = c_max
    
    #Calculate hue based on channel maximum
    if diff == 0:
        h = 0
    elif c_max == r:
        h = (60*(g-b)/(diff))%360
    elif c_max == g:
        h = (60*(b-r)/(diff)+120)%360
    elif c_max == b:
        h = (60*(r-g)/(diff)+240)%360
    
    #Calculate saturation
    if c_max == 0:
        s = 0
    else:
        s = diff/c_max
    
    #Rescale between 0 to 255
    h = h*255/360
    s *= 255
    v *= 255
        
    return h,s,v
def convert_to_hsv(rgb_image):
    height, width, depth = rgb_image.shape
    hsv = np.zeros(height, width, depth) #Creates placeholder array for values
    #Loops through each pixel and converts to hsv
    for i in range(height):
        for j in range(width):
            R, G, B = rgb_image[i, j, 0:3]
            hsv[i,j] = rgb_to_hsv(int(R), int(G), int(B))
    hsv.astype(np.uint8)
    return hsv
def main():
    path = input("Enter the path of the RGB image you want to convert to hsv: ")
    img_array = load_img(path)
    hsv = convert_to_hsv(img_array)
    # Resize to fit within 100 x 100 while keeping the aspect ratio
    orig_height, orig_width = img_array.shape[:2]
    orig_aspectRatio = orig_width / orig_height
    target_aspectRatio = 100 / 100
    if orig_aspectRatio >= target_aspectRatio:
        new_width = 100
        new_height = int(100 / orig_aspectRatio)
    else:
        new_height = 100
        new_width = int(100 * orig_aspectRatio)
    resized_img = resize_image(hsv, (new_width, new_height))
    padded_img = pad_image(resized_img, (100, 100))
    pixel_coords = input("Enter the coordinates of the pixel you want inspect: ")
    pixel_x, pixel_y = tuple(int(x) for x in pixel_coords.split(", "))
    print(f"RGB values of the ({pixel_x}, {pixel_y}) pixel: R={img_array[pixel_x,pixel_y,0]}, G={img_array[pixel_x,pixel_y,1]}, B={img_array[pixel_x,pixel_y,2]}")
    print(f"Converting {path} to HSV...")
    print(f"HSV values of the ({pixel_x}, {pixel_y}) pixel: H={hsv[pixel_x,pixel_y,0]}, S={hsv[pixel_x,pixel_y,1]}, V={hsv[pixel_x,pixel_y,2]}")


    plt.imshow(padded_img)
    plt.axis("off")
    plt.show()
    

if __name__ == "__main__":
    main()
