import cv2
import numpy as np


## Reading image

img = cv2.imread("Ressources/Benz.png")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB colored image", img2)
cv2.waitKey(0)

## Reading video or cam feed

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break