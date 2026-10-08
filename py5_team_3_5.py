"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py5 Team 3
    Team ID:        SC1 - 05
    Author:         Edison Zheng, zhen1058@purdue.edu
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
from PIL import ImageOps
import matplotlib.pyplot as plt


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
def main():
    # Load the image the user asks for
    image_path = input("Enter the path of the image you want to clean: ")
    img_array = load_img(image_path)
    # Only scale to 0-255 if load_img returned floats (0-1); uint8 is left alone
    if img_array.dtype != np.uint8:
        img_array = (img_array * 255).astype(np.uint8)
    # NumPy shape is (height, width, ...)
    orig_height, orig_width = img_array.shape[:2]

    # Input looks like "100, 100": split on the comma and convert each part to an int
    target_size = tuple(int(x) for x in input("Enter the target width and height: ").split(","))
    print(f"Image shape before cleaning: {(orig_width, orig_height)}")

    # Compare aspect ratios (width / height) to decide which side limits the resize
    orig_aspectRatio = orig_width / orig_height
    target_aspectRatio = target_size[0] / target_size[1]

    if orig_aspectRatio >= target_aspectRatio:
        # Image is relatively wider: width fills the target, height shrinks to match
        new_width = target_size[0]
        new_height = int(target_size[0] / orig_aspectRatio)
    else:
        # Image is relatively taller: height fills the target, width shrinks to match
        new_height = target_size[1]
        new_width = int(target_size[1] * orig_aspectRatio)

    # Resize while keeping the aspect ratio, then pad up to the target size
    resized_img = resize_image(img_array, (new_width, new_height))
    print(f"Image shape after resizing: {(resized_img.shape[1], resized_img.shape[0])}")
    padded_img = pad_image(resized_img, target_size)
    print(f"Image shape after cleaning: {(padded_img.shape[1], padded_img.shape[0])}")

    # Display the final padded image without axis ticks
    plt.imshow(padded_img)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()