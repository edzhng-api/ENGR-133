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
from PIL import Image
import matplotlib.pyplot as plt

def linearize_image(image_array):
    return np.where(
        image_array <= 0.04045,
        image_array / 12.92,
        ((image_array + 0.055) / 1.055) ** 2.4,
    )

def load_img(path): #Opens the image, converts it to RGB if it has an alpha channel, normalizes it, and linearizes it.
    with Image.open(path) as pil_image:
        if "A" in pil_image.getbands():
            pil_image = pil_image.convert("RGB")
        image_array = np.array(pil_image)
    normalized_image = normalize_image(image_array)
    return linearize_image(normalized_image)

def normalize_image(image_array):
    return image_array.astype(float) / 255.0

def rgb_to_grayscale(rgb_image):
    R = np.array(rgb_image)[:,:,0]
    G = np.array(rgb_image)[:,:,1]
    B = np.array(rgb_image)[:,:,2]
    Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
    return Y

def main():
    image_path = input("Enter the path of the image you want to load: ")

    # load_img converts, normalizes, and linearizes the image.
    linearized_image = load_img(image_path)

    if len(linearized_image.shape) == 2:  # Check if the image is already grayscale
        plt.imshow(linearized_image, cmap='gray')
    else:
        convert = input("Would you like to convert to grayscale? ")
        if convert == "yes":
            grayscale_image = rgb_to_grayscale(linearized_image)
            plt.imshow(grayscale_image, cmap='gray')
        else:
            plt.imshow(linearized_image, cmap='gray')
    plt.axis('off')  # Hide axes
    plt.show()

if __name__ == "__main__":
    main()
