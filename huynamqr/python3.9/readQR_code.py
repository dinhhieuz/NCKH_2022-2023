import cv2 as cv
from pyzbar.pyzbar import decode


cam = cv.VideoCapture(0)
cam.set(5, 640)
cam.set(6, 480)

camera = True
while camera == True:
    success, frame = cam.read()
    for i in decode(frame):
        print(i.type)
        print(i.data.decode('utf-8'))

        cv.imshow('OurQr_Code_Scanner', frame)
        cv.waitKey(1)



