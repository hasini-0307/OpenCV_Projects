
import cv2
import numpy as np

frameWidth = 480
frameHeight = 360
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 130)

# HSV ranges: [H_min, S_min, V_min, H_max, S_max, V_max]
myColors = [[5, 57, 127, 179, 255, 255],     # Orange
            [100, 150, 0, 130, 255, 255],    # Blue
            [20, 100, 100, 30, 255, 255 ]] # yellow

myColorValues = [[0,140,255],[255,0,0],[30,255,255]] #BGR
myPoints = [] #[x,y,colorId]

def findColors(img, myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count =0
    newPoints =[]
    for i, color in enumerate(myColors):
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        mask_resized = cv2.resize(mask, (320, 240))
        x,y= getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count += 1
        #cv2.imshow(f"Mask {i+1}", mask_resized)  # Show each mask in a separate window
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area>500:
           # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)

            cornerPts = cv2.approxPolyDP(cnt,0.02*peri,True)

            x,y,w,h =  cv2.boundingRect(cornerPts)
    return x+w//2,y
def DrawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)



while True:
    success, img = cap.read()
    imgResult = img.copy()

    newPoints = findColors(img, myColors,myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints) !=0:
        DrawOnCanvas(myPoints, myColorValues)


    img_resized = cv2.resize(img, (320, 240))
    cv2.imshow("virtual paint", imgResult)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()






