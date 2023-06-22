#this one is supposed to identify frontal faces

#importing 
import numpy as np
import cv2 as cv
import pytesseract

#I can apply most of this stuff when using a camera

face_classifier = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

"""Reading image, converting color to grayscale. 
Converting grayscale image into a black and white one, syntax (sourceimg, threshold value, maximum value and a thresholding method)
THRESH_BINARY -> sets pixels with higher intensity value to maximum value (w) and 
pixels with intensity values below the threshold to 0 (b)
"""

image_r = cv.imread('CNH_ex2.jpeg')
img_gray = cv.cvtColor(image_r, cv.COLOR_BGR2GRAY)
img_bw = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)[1]

"""image = cv.imread('girlface_test.png', cv.IMREAD_GRAYSCALE)
image_gray = cv.cvtColor(image, cv.COLOR_GRAY2BGR)
colored_img = cv.cvtColor(image_gray, cv.COLOR_BGR2HSV)

colored_img[1, 1, 1] = np.clip(colored_img[1,1,1]*5, 0, 255).astype(np.uint8)
colored_img[0, 0, 0] = np.clip(colored_img[0,0,0]*5, 0, 255).astype(np.uint8)
colored_img[0, 0, 0] = np.clip(colored_img[0,0,0]*5, 0, 255).astype(np.uint8)

img_hsv = cv.cvtColor(colored_img, cv.COLOR_HSV2BGR)"""

faces = face_classifier.detectMultiScale(img_bw, 1.1, 5)

for(x,y,w,h) in faces:
    cv.rectangle(img_bw, (x,y), (x+w, y+h), (0,0,255),2)

cv.imshow('imagem',img_bw)
cv.waitKey(0)
cv.destroyAllWindows() 
