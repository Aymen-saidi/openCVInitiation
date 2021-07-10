import cv2
import numpy as np

##Wrapign an image
img = cv2.imread("Ressources/Cards.jpg")
width,height = 250,350
pts1 = np.float32([[327,313],[603,94],[598,674],[927,500]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image", img)
cv2.imshow("Ouput wrapped img", imgOutput)



## Joining two images horizentally and vertically
img = cv2.imread("D:/aymen/BIGFOLDER/overhaul.jpg")
#(810, 1440, 3)
img1 = cv2.resize(img,[600,1000])
hor = np.hstack((img1,img1))
ver = np.vstack((imgOutput,imgOutput))
cv2.imshow("horizental", hor)
cv2.imshow("horizentally joint", img1)
cv2.imshow("vertically joint", ver)
cv2.waitKey()
