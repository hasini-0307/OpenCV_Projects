import cv2   # core openCV library toolkit for computer vision
from cvzone.HandTrackingModule import HandDetector
 # a helper class from CVZone for detecting hands easily.

cap = cv2.VideoCapture(0)  # default webcam- (0)
cap.set(3, 1280) # frame width
cap.set(4, 720) # frame height

detector  = HandDetector(detectionCon=0.8,maxHands=2)
#detector object           min  confidence  in detecting hands-80%
# confidence thresholds are tunable parameters.
startDist = None
scale = 0
cx,cy =640,360


#startDist → distance between fingers when zoom gesture starts.
#scale → how much to zoom in/out.
#cx, cy → center of the zoom (defaults to middle of screen).

while True:
    #Infinite loop to continuously capture frames.Needed for real time video capturing.
    success , img = cap.read()
    # reads one frame from camera
    #success - boolean if read worked . img - actual frame(np array)
    if not success: break
    hands , img = detector.findHands(img)
    # hands - list of detected hand info
    img1 = cv2.imread("zoom_gesture.jpg")
    h1, w1, _ = img1.shape
    # load overlay image.
    if len(hands) == 2:
        # Checks if two hands are visible.

        #print(detector.fingersUp(hands[0]), detector.fingersUp(hands[1]))

        if detector.fingersUp(hands[0]) == [1,1,0,0,0] and\
            detector.fingersUp(hands[1]) == [1,1,0,0,0]:

           # fingersUp - returns list of 5 values (1=open, 0=closed).
           #  Condition checks both hands show same gesture.To confirm user is doing zoom gesture.
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]

           #lmList = list of 21 landmarks per hand.
            # point 8 is the tip of the index finger

            x1, y1 = lmList1[8][0:2]  # take only the (x,y)- coordinates for hands in the frame.
            x2, y2 = lmList2[8][0:2]
            if startDist == None:  # initial distance setup. "GESTURE NORMALIZATION"
                length, info, img = detector.findDistance((x1, y1), (x2, y2), img)
                print(length)
                startDist = length
                cx , cy = info[4:]
#update zoomscale. Measure new dist. ZOOM SCALE = DIFF. FROM START DIST.
            length, info, img = detector.findDistance((x1, y1), (x2, y2), img)
            scale = int((length- startDist)//2) # //2 - FOR SMOOTH SCALING .
            print(scale)

    else:
        # less than 2 hands RESET GESTURE STATE
        startDist = None
    try:
        # apply zoom transformation.
        newH = max(50, ((h1 + scale) // 2) * 2)  # prevent <=0
        newW = max(50, ((w1 + scale) // 2) * 2)
#Force even numbers (*2) for safe resizing.
        #This is the core of the “zoom effect”.
        imgResized = cv2.resize(img1, (newW, newH))
# defining overlay region
        top = max(0, cy - newH // 2)
        bottom = min(img.shape[0], cy + newH // 2)
        left = max(0, cx - newW // 2)
        right = min(img.shape[1], cx + newW // 2)
        #Calculates rectangular region where the zoomed image will be placed.
# img.shape[0] = height, img.shape[1] = width

     #Actual size of region of interest (ROI).
        roiH = bottom - top
        roiW = right - left


    #Replaces part of the video frame with zoomed image.
        # This is where the “virtual zoom” becomes visible.
        img[top:bottom, left:right] = imgResized[0:roiH, 0:roiW]

    except: # EXCEPTION HANDLING
        pass
    cv2.imshow("Image", img) # show output

    key = cv2.waitKey(1) & 0xFF # delay and exit key 'q' to stop.
    if key == ord('q'):
        break












