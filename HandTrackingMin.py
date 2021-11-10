from cv2 import cv2
import time

import mediapipe as mp

# To get hand model from mediapipe
mpHand = mp.solutions.hands
# To set parameters
hands = mpHand.Hands()
# To draw connections between landmarks
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

previousTime = 0
currentTime = 0
while True:
    success, img = cap.read()

    # //to detect hand
    # send rgb image to object hands
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)  # will process frame for us and give result
    # print(results.multi_hand_landmarks)
    # now extract result from hands if hands is not None
    if results.multi_hand_landmarks:
        for singleHand in results.multi_hand_landmarks:
            # get id and landmarks(x y coordinates)
            for id, lm in enumerate(singleHand.landmark):
                # print(id, lm) if we print this well get landmark id and x,y coordinates 20 x:0.93294 y:0.34723894 and so on other landmarks
                # x and y coordinates will help us find location of the landmark on the hand
                # to get pixel value multiply with width and height
                height, width, chanel = img.shape
                pixelX, pixelY = int(lm.x * width), int(lm.y * height)
                # print(id, pixelX, pixelY)
                if (id == 0):
                    cv2.circle(img, (pixelX, pixelY), 20, (255, 0, 255), cv2.FILLED)

            # mediapipe provided us with function that will draw landmarks
            # otherwise there will be a lot of math for drawinf dots and connecting
            mpDraw.draw_landmarks(img, singleHand, mpHand.HAND_CONNECTIONS)

    currentTime = time.time()
    # This frequency is usually measured by frames per second (fps). For example, at 30 fps, 30 distinct images would appear in succession within one second
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_ITALIC, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
