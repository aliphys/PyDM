"""
Python script to read and decode datamatrix barcodes
"""


# pip install opencv-python #module needs to be installed, if not already
import cv2                                  # OpenCV library is cool. Has lots of functions to handle images
from pylibdmtx.pylibdmtx import decode      # this is th module that does the date matrix handling stuff
from PIL import Image                       # because without importing images, nothing will work :) 

image = cv2.imread("IMG_20230504_174150.jpg")       #Replace filename, with your image

# Apply median filtering for noise removal since there are weird stuff in the image. 
denoised = cv2.medianBlur(image, 1)

# Threshold the denoised image
_, thresholded = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

h, w  = image.shape[:2]                             # since barcode can be small, we may need to sharpen it up a bit
decdd = decode((image[:, :, :1].tobytes(), w, h))   # one channel is enough. who care about color anyway
#print(decdd)                                        #print the information to the terminal

# Print the decoded message
if decdd:
    message = decdd[0].data.decode()
    print("Decoded Message:", message)
else:
    print("DataMatrix decoding failed.") # this way I know what is going on

# Display the denoised and thresholded images
cv2.imshow("Denoised Image", denoised)
cv2.imshow("Thresholded Image", thresholded)
cv2.waitKey(0) #wait for key press
cv2.destroyAllWindows()
