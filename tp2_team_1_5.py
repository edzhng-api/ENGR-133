"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     TP2 Team 1
    Team ID:        SC1 - 05
    Author:         Edison Zheng, zhen1058@purdue.edu
    Date:           10/22/2026

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
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import math as m


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
    #Convert an RGB image to one luminance value per pixel.
    R = np.array(rgb_image)[:,:,0]
    G = np.array(rgb_image)[:,:,1]
    B = np.array(rgb_image)[:,:,2]
    Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
    return Y

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

def apply_kernel(image, kernel):
    rows, cols = image.shape
    k_rows, k_cols = kernel.shape
    # Pad image with zeros
    padded = np.pad(image,((k_rows // 2, k_rows // 2), (k_cols // 2, k_cols // 2)),mode='constant', constant_values=0)
    # Create array of 0s having the same shape as the original image
    output = np.zeros(rows, cols)
    for i in range(rows):
        for j in range(cols):
            # Slice the padded image, add the output to output array
            window = padded[i:i + k_rows, j:j + k_cols]
            output[i, j] = np.sum(window * kernel)
    return output

def sobel_filter(grayscale_img):
    sobel_x = np.array([[-1,0,1],
                       [-2,0,2],
                       [-1,0,1]], dtype=float)
    sobel_y = np.array([[-1,-2,-1],
                       [0,0,0],
                       [1,2,1]], dtype=float)
    img_array = np.array(grayscale_img, dtype=float)
    rows, columns = img_array.shape
    combined_img = np.zeros(rows, columns)
    
    x_gradient = apply_kernel(img_array, sobel_x)
    y_gradient = apply_kernel(img_array, sobel_y)
    rows_g, columns_g = x_gradient.shape
    
    for i in range(rows_g):
        for j in range(columns_g):
            combined_img[i,j] = m.sqrt(x_gradient[i,j]**2 + y_gradient[i,j]**2)
            if combined_img[i,j] > 255:
                combined_img[i,j] = 255
                
    for i in range(rows):
        for j in range(columns):
            if combined_img[i,j] >= 50:
                combined_img[i,j] = 255
            else:
                combined_img[i,j] = 0
    combined_img = combined_img.astype(np.uint8)
    return combined_img
def main():
    """Write your code here (and delete this line)."""


if __name__ == "__main__":
    main()
