import cv2
import numpy as np
def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("HueMin","TrackBars",0,179,empty)
cv2.createTrackbar("HueMax","TrackBars",0,179,empty)
cv2.createTrackbar("SatMin","TrackBars",0,255,empty)
cv2.createTrackbar("SatMax","TrackBars",255,255,empty)
cv2.createTrackbar("ValMin","TrackBars",0,255,empty)
cv2.createTrackbar("ValMax","TrackBars",255,255,empty)



while True:
    img = cv2.imread("Ressources/Lambo.jpg")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("HueMin", "TrackBars")
    h_max = cv2.getTrackbarPos("HueMax", "TrackBars")
    s_min = cv2.getTrackbarPos("SatMin", "TrackBars")
    s_max = cv2.getTrackbarPos("SatMax", "TrackBars")
    v_min = cv2.getTrackbarPos("ValMin", "TrackBars")
    v_max = cv2.getTrackbarPos("ValMax", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)



    #cv2.imshow("lamborghini car", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("lamborghini HSV", imgHSV)
    cv2.waitKey(1)