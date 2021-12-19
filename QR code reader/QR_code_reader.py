import cv2
import numpy as np
from pyzbar.pyzbar import decode

# This Project Is Developed By Shailendra Singh Admin Of @Python_Coderz_ Page - Instagram
# Dm Us If You Have Any Query- https://www.instagram.com/python_Coderz_/

cap = cv2.VideoCapture(0)
cap.set(3,640) #width of the frames in the video feed
cap.set(4,480) #height of the frames in the video feed

while True:
    ret,img = cap.read()
    for barcode in decode(img):
        mydata = barcode.data.decode('utf-8')
        print(mydata)
        pts = np.array([barcode.polygon],np.int32)
        pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(0,0,255),5)
        pts2 = barcode.rect
        cv2.putText(img,mydata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,255,255),3)

    cv2.imshow('answer',img)
    cv2.waitKey(1)
cv2.destroyAllWindows()

