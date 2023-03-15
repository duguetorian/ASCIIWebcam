import os
import cv2
import numpy as np
import math as mt

ascii_density_string = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,"^`\'. '[::-1]

def ascii_conversion(frame, color):
    height = os.get_terminal_size().lines - 1
    image = grayscale_conversion(frame)
    size = np.shape(image)
    ascii_image = '\r'
    # print(image[0,0])

    for i in range(size[0]):
        for j in range(size[1]):
            if color:
                px = frame[i, -j]
                # Add color for the char
                ascii_image += f'\033[38;2;{px[2]};{px[1]};{px[0]}m'
            # Convert to ascii
            ascii_image += ascii_density_string[mt.floor(image[i, -j]*(len(ascii_density_string)-1)/255)]
        ascii_image += "\n"
    
    print(size[0] <= height, size[0], height)
    if size[0] < height:
        print("".join(["\n" for i in range(height - size[0])]))

    return ascii_image[:-1]

def grayscale_conversion(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# \033[38;2;255;0;0m