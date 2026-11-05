"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     7.2.2 tp1 team 2 
    Team ID:        SC1 - 05
    Author:         Anthony Do, do132@purdue.edu
                    Edison Zheng, zhen1058@purdue.edu
                    Reese Jared, rjared@purdue.edu
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
from PIL import Image, ImageOps
import numpy as np
# Create square kernel
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
def main():
    kernel_size = int(input('Enter kernel size: '))
    kernel = create_mean_kernel(kernel_size)
    # Return if the kernel isnt valid
    if kernel is None:
        print('Invalid kernel size: must be a positive odd number')
        return
    image = np.array([
        [0,  0,   0,  0, 0],
        [0,  0,   0,  0, 0],
        [0,  0, 255,  0, 0],
        [0,  0,   0,  0, 0],
        [0,  0,   0,  0, 0],
    ], dtype=float)
    filtered = apply_kernel(image, kernel)
    # Display settings
    np.set_printoptions(precision=6)
    # Display
    print(f'Kernel size: {kernel_size}x{kernel_size}')
    print(f'Kernel sum: {kernel.sum():.6f}')
    print('Kernel:')
    print(kernel)
    print()
    print('Filtered image:')
    print(filtered)

if __name__ == '__main__':
    main()