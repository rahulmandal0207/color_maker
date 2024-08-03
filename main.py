import numpy as np
import cv2 as cv

def test(x):
    pass

img = np.zeros((300,512,3), np.uint8)
cv.namedWindow("Trackbars")

cv.createTrackbar("R","Trackbars",0, 255, test)
cv.createTrackbar("G","Trackbars",0, 255, test)
cv.createTrackbar("B","Trackbars",0, 255, test)

while True:    
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    r = cv.getTrackbarPos("R", "Trackbars")
    g = cv.getTrackbarPos("G", "Trackbars")
    b = cv.getTrackbarPos("B", "Trackbars")

    hex_code = f'#{r:02x}{g:02x}{b:02x}'

    print(hex_code)

    img[:] = [b,g,r]

    cv.imshow("Trackbars", img)
cv.destroyAllWindows()