import cv2
import numpy as np

def getContours(img):
    contours, hierachy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 2)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3: ObjectType="Tri"
            elif objCor == 4: ObjectType="4 thing"
            elif objCor == 6: ObjectType="Losange"
            elif objCor >= 8: ObjectType="Circle"
            else:ObjectType="None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,ObjectType,
                        (x+(w//2),y+(h//2)),cv2.FONT_HERSHEY_SIMPLEX,0.5,
                         (0,0,0),2)


img = cv2.imread("Ressources/filled_shapes.jpg")
imgContour = img.copy()
Grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
Blurimg = cv2.GaussianBlur(Grayimg,(7,7),1)
Cannyimg = cv2.Canny(Blurimg,50,50)
getContours(Cannyimg)




cv2.imshow("Cannied shapes", Cannyimg)
cv2.imshow("Gray shapes", Grayimg)
cv2.imshow("Blurred shapes", Blurimg)
cv2.imshow("shapes", img)
cv2.imshow("Contoured image", imgContour)
cv2.waitKey()