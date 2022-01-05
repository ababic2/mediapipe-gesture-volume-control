import cv2
import numpy as np
import pygame
import HandTrackingModule as htm
import math  # for hypoteuns function

wCam, hCam = 1280, 720
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionConfidence=0.7)

pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
pygame.mixer.init()
sound1 = pygame.mixer.Sound("flaunt.ogg")
minVol = 0
maxVol = 1

vol = 0
volBar = 400
volPer = 0

sound1.play()

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
        # Convert distance value
        # Hand range was [30, 300]
        # [0, 1] is the range to which we want to convert it
        vol = np.interp(distance, [30, 300], [0, 1])
        volBar = np.interp(distance, [30, 300], [400, 150])
        volPer = np.interp(distance, [30, 300], [0, 100])
        sound1.set_volume(vol)

        if distance < 30:
            # button effect
            cv2.circle(img, (centerLineX, centerLineY), 10, (255, 0, 0), cv2.FILLED)
    cv2.rectangle(img, (50, 150), (85, 400), (0,255,0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)}%', (40,450), cv2.FONT_HERSHEY_COMPLEX,1 ,(0,255,0), 3)

    cv2.imshow('MediaPipe Hands', img)
    cv2.waitKey(1)
