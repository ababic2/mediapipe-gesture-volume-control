import cv2
import numpy as np
import time
import HandTrackingModule as htm
import math #for hypoteuns function
import pycaw

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam, hCam = 1280, 720
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionConfidence=0.7)

#PYCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
print(volume.GetVolumeRange())
# volume.SetMasterVolumeLevel(-20.0, None)


while True:
    success, img = cap.read()
    img = detector.findHand(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        centerLineX, centerLineY = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(img, (centerLineX, centerLineY), 10, (255, 210, 0), cv2.FILLED)
        # finding distance between two landmarks
        # distance bewteen 2 coordinates is d= sqrt((x2-x1)^2 + (y2-y1)^2)
        distance = math.hypot((x2 - x1), (y2 - y1))
        # print(distance)
        if distance < 30:
            #button effect
            cv2.circle(img, (centerLineX, centerLineY), 10, (255, 0, 0), cv2.FILLED)
    cv2.imshow('MediaPipe Hands', cv2.flip(img, 1))
    cv2.waitKey(1)
