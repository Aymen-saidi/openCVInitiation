import cv2
import numpy as np
# faceCascade = cv2.CascadeClassifier("Ressources/haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread('Ressources/MF.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(imgGray,1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)




cv2.imshow("Megan fox", img)
# cv2.imshow("Gray MF", imgGray)
cv2.waitKey(0)