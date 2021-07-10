import cv2
import numpy as np

#The under lien helps to read with URL from computer
img = cv2.imread("C:/Users/aymen/Desktop/samples.png")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgGray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
imgBlur =cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dilate(imgCanny, kernel = np.ones((5, 5), np.uint8), iterations=1)
imgErosion = cv2.erode(imgDialation,kernel = np.ones((5, 5), np.uint8), iterations=1)



cv2.imshow("Gray image", imgGray)
cv2.imshow("Blurred image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dialated image", imgDialation)
cv2.imshow("Erode image", imgErosion)

cv2.waitKey(0)


img = cv2.imread("Ressources/Lambo.jpg")
cv2.imshow("Lamborghini", img)
print(img.shape)
imgCropped = img[0:200,200:500]
cv2.imshow("Cropped image", imgCropped)
print(imgCropped.shape)

cv2.waitKey(0)
