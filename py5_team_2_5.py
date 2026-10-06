"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     17.2.2 Py5 Team 2
    Team ID:        SC1 - 05
    Author:         Reese Jared, rjared@purdue.edu
    Date:           10/06/2026

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
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageOps

def linearize(c):
    return np.where(
        c <= 0.04045,
        c / 12.92,
        ((c + 0.055) / 1.055) ** 2.4,
    )

def load_img(path):
    image_array = np.array(Image.open(path))
    float_image_array = image_array.astype(float) / 255.0  # Normalize to [0, 1]
    linearized_image_array = linearize(float_image_array)
    return linearized_image_array

def rgb_to_grayscale(rgb_image):
    R = np.array(rgb_image)[:,:,0]
    G = np.array(rgb_image)[:,:,1]
    B = np.array(rgb_image)[:,:,2]
    Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
    return Y

def main():
    image_path = load_img(input("Enter the path of the image you want to load: "))
    if len(image_path.shape) == 2:  # Check if the image is already grayscale
        plt.imshow(image_path, cmap='gray')
    else:
        convert = input("Would you like to convert to grayscale? ")
        if convert == "yes":
            grayscale_image = rgb_to_grayscale(image_path)
            plt.imshow(grayscale_image, cmap='gray')
        else:
            plt.imshow(image_path, cmap='gray')
    plt.axis('off')  # Hide axes
    plt.show()

if __name__ == "__main__":
    main()
