"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     e.g. 7.2.1 Py1 Team 1 (for Python 1 Team task 1)
    Team ID:        SC1 - 05
    Author:         Name, login@purdue.edu
    Date:           e.g. 01/23/2026

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

def create_mean_kernel(kernel_size):
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
    value = 1 / (2 * np.pi * sigma ** 2) * np.e ** (-((x - kernel_size // 2) ** 2 + (y - kernel_size // 2) ** 2) / (2 * sigma ** 2))
    return value

def create_gaussian_kernel(sigma):
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
    # Pad image with zeros
    padded = np.pad(image,((kernel_size // 2, kernel_size // 2), (kernel_size // 2, kernel_size // 2)),mode='constant', constant_values=0)
    return padded

def gaussian_filter(image, sigma):
    kernel = create_gaussian_kernel(sigma)
    kernel_size = kernel.shape[0]
    padded_image = apply_padding(image, kernel_size)
    filtered_image = np.zeros(image.shape, dtype=float)

    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            window = padded_image[row:row + kernel_size, col:col + kernel_size]
            filtered_image[row, col] = np.sum(window * kernel)

    return filtered_image

def main():
    image_path = input("Enter the path to the image file: ")
    load_img 
    sigma = 1
    if sigma <= 0:
        return print("Sigma must be positive.")
    total = np.sum(create_gaussian_kernel(sigma))
    print(f"Total sum of Gaussian kernel values: {total}")
    plt.imshow(create_gaussian_kernel(sigma), cmap='gray')
    plt.show()

if __name__ == "__main__":
    main()
