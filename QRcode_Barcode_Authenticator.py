# ID AUTHENTICATION USING QR AND BARCODE .

import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('IDCARDMURTAZA.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
with open('myData.text') as f:
    myDataList = f.read().splitlines()


while True:
    success , img = cap.read()
    code =decode(img)
    for barcode in code:

        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData  in myDataList:
            myOutput = 'Authorized'
            myColor = (0,255,0)
        else:
            myOutput= 'Un-authorized'
            myColor = (0, 0,255)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        x, y = pts[0][0]
        cv2.putText(img, myOutput, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
    cv2.imshow("results",img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press 'q' to quit
        break

