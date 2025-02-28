import cv2
import matplotlib.pyplot as plt
import numpy as np

# original image
image = cv2.imread("img.jpeg")
cv2.imshow(" Original Image", image)
cv2.waitKey(0)

#image brightness
plt.subplot(1, 2, 1) 
plt.title("Original") 
plt.imshow(image)  
brightness = 10  
contrast = 2.3  
image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness) 

#adding border to an image
borderoutput = cv2.copyMakeBorder( 
image, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255, 255, 0]) 
cv2.imshow(" Bordered Image", borderoutput )
cv2.waitKey(0)

#negative the image
img_bgr = cv2.imread('swan.jpg', 1) 
color = ('b', 'g', 'r')  
for i, col in enumerate(color): 
    histr = cv2.calcHist([img_bgr], [i], None, [256], [0, 256]) 
    plt.plot(histr, color = col) 
    plt.xlim([0, 256])      
plt.show()

#BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
cv2.imshow('image', image_rgb) 
cv2.waitKey(0)

#cropping an image
crop = image[50:180, 100:300]   
cv2.imshow('original', image) 
cv2.imshow('cropped', crop) 
cv2.waitKey(0) 

# gray scale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

# rotate 90 degree
image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated image', image)
cv2.waitKey(0)

# blurring the image
avging = cv2.blur(image,(10,10))
cv2.imshow('Averaging',avging)
cv2.waitKey(0)

# Resize the image
half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
bigger = cv2.resize(image, (1050, 1610))

stretch_near = cv2.resize(image, (780, 540), 
               interpolation = cv2.INTER_LINEAR)


Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[image, half, bigger, stretch_near]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()

# Close all windows
cv2.destroyAllWindows()
