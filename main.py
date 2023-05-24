"""
Python script to read and decode datamatrix barcodes
"""


# pip install opencv-python #module needs to be installed, if not already
import cv2                                  # OpenCV library is cool. Has lots of functions to handle images
from pylibdmtx.pylibdmtx import decode      # this is th module that does the date matrix handling stuff
from PIL import Image                       # because without importing images, nothing will work :) 

image = cv2.imread("IMG_20230504_174150.jpg")       #Replace filename, with your image
h, w  = image.shape[:2]                             # since barcode can be small, we may need to sharpen it up a bit
decdd = decode((image[:, :, :1].tobytes(), w, h))   # one channel is enough. who care about color anyway
print(decdd)                                        #print the information to the terminal
