"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    This program applies a Gaussian filter to an RGB image from a path that was prompted for and coonverted to grayscale.

Assignment Information:
    Assignment:     7.2.3 tp1 team 3
    Team ID:        SC1 - 05
    Author:         Reese Jared, rjared@purdue.edu
                    Anthony Do, do132@purdue.edu
                    Edison Zheng, zhen1058@purdue.edu
                    Gibson Lamb, lamb112@purdue.edu
    Date:           10/17/2026

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

def create_mean_kernel(kernel_size):
    #Create a square averaging kernel for a positive odd size.

    # If kernel not odd or positive then return None
    if kernel_size % 2 != 1 or kernel_size <= 0:
        return
    # Empty list
    kernel_list = []
    for i in range(kernel_size):
        col = []
        for j in range(kernel_size):
            value = 1 / (kernel_size**2)
            col.append(value)
        kernel_list.append(col)
    # Turn the list to kernel array
    return np.array(kernel_list)

def create_gaussian_value(sigma, kernel_size, x, y):
    #Calculate the Gaussian weight at one kernel coordinate.
    value = 1 / (2 * np.pi * sigma ** 2) * np.e ** (-((x - kernel_size // 2) ** 2 + (y - kernel_size // 2) ** 2) / (2 * sigma ** 2))
    return value

def create_gaussian_kernel(sigma):
    #Build and normalize a square Gaussian kernel for the given sigma.
    kernel_size = int(2 * np.ceil(3 * sigma) + 1)
    kernel_list = []
    for i in range(kernel_size):
        col = []
        for j in range(kernel_size):
            value = create_gaussian_value(sigma, kernel_size, i, j)
            col.append(value)
        kernel_list.append(col)
    kernel = np.array(kernel_list)
    return kernel / np.sum(kernel)

def apply_padding(image, kernel_size):
    #Add a zero-valued border so filtering also covers image edges.
    padded = np.pad(image,((kernel_size // 2, kernel_size // 2), (kernel_size // 2, kernel_size // 2)),mode='constant', constant_values=0)
    return padded

def linearize_image(image_array):
    #Convert normalized sRGB channel values to linear-light values.
    return np.where(
        image_array <= 0.04045,
        image_array / 12.92,
        ((image_array + 0.055) / 1.055) ** 2.4,
    )

def normalize_image(image_array):
    #Convert integer image channels from 0-255 to floating-point 0-1.
    return image_array.astype(float) / 255.0

def load_img(path):
    #Open an image, remove transparency if present, and prepare its values.
    with Image.open(path) as pil_image:
        # This program processes color channels, not transparency.
        if "A" in pil_image.getbands():
            pil_image = pil_image.convert("RGB")
        image_array = np.array(pil_image)
    normalized_image = normalize_image(image_array)
    return linearize_image(normalized_image)

def rgb_to_grayscale(rgb_image):
    #Convert an RGB image to one luminance value per pixel.
    R = np.array(rgb_image)[:,:,0]
    G = np.array(rgb_image)[:,:,1]
    B = np.array(rgb_image)[:,:,2]
    Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
    return Y

def gaussian_filter(image, sigma):
    #Blur a two-dimensional image with a normalized Gaussian kernel.
    kernel = create_gaussian_kernel(sigma)
    kernel_size = int(2 * np.ceil(3 * sigma) + 1)
    padded_image = apply_padding(image, kernel_size)
    filtered_image = np.zeros(image.shape, dtype=float)

    # Move the kernel over every image position and sum weighted neighbors.
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            window = padded_image[row:row + kernel_size, col:col + kernel_size]
            filtered_image[row, col] = np.sum(window * kernel)

    return filtered_image.astype(np.uint8)

def main():
    #Load an image, blur its grayscale version, and display the result.
    sigma = 1
    image_path = input("Enter the path to the image file: ")
    image = load_img(image_path)
    # Convert color images to luminance; grayscale inputs can be used directly.
    if len(image.shape) == 3:  # Check if the image is RGB
        image = rgb_to_grayscale(image)
    # The filter works with 0-255 intensities, while load_img returns 0-1.
    filtered_image = gaussian_filter(image * 255, sigma)
    normalized_filtered_image = filtered_image / 255
    # Convert linear-light values back to sRGB for an accurate display.
    display_image = np.where(
        normalized_filtered_image <= 0.0031308,
        normalized_filtered_image * 12.92,
        1.055 * normalized_filtered_image ** (1 / 2.4) - 0.055,
    )
    plt.imshow(display_image, cmap='gray', vmin=0, vmax=1)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
