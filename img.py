import cv2
import matplotlib.pyplot as plt

# original image
image = cv2.imread("img.jpeg")
cv2.imshow(" Original Image", image)
cv2.waitKey(0)

# gray scale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

# rotate 90 degree
image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated image', image)
cv2.waitKey(0)

# rotate 180 degree
image = cv2.rotate(image, cv2.ROTATE_180)
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