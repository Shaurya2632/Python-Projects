import cv2
import numpy as np
from enum import IntEnum

# short keys
wait = lambda sec: cv2.waitKey(sec * 1000)
resize = lambda img, width, height: cv2.resize(img, (width, height))

# Classes
class Channels(IntEnum):
    GRAYSCALE = 0
    COLORFUL = 1
    RGB = 2
    RGBA = 3
    CMYK = 4
    YCBCR = 5
    HSV = 6
    LAB = 7

# functions
def split(img, Hor=1, Ver=1):

    h = np.vstack(tuple([img for _ in range(Hor)]))
    v = np.hstack(tuple([h for _ in range(Ver)]))

    return v

def RGB(R, G, B):

    return B, G, R

# main

img = cv2.imread(r'E:\coding\python\Images\Bird.jpg')
img = resize(img, 400, 500)

img = cv2.Canny(img, 400, 600)

cv2.imshow("", img)
wait(0)
