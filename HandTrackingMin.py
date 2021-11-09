from cv2 import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHand = mp.solutions.hands #to get a hand model from mp
hands = mpHand.Hands() #check parameters and video on 6:50
mpDraw = mp.solutions.drawing_utils
while True:
    success, img = cap.read()

    # //to detect hand
    #send rgb image to object hands
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB) #will process frame for us and give result
    #print(results.multi_hand_landmarks)
    #now extract result from hands if hands is not None
    if results.multi_hand_landmarks:
        for singleHand in results.multi_hand_landmarks:
            #mediapipe provided us with function that will draw landmarks
            #otherwise there will be a lot of math for drawinf dots and connecting
            mpDraw.draw_landmarks(img, singleHand, mpHand.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    cv2.waitKey(1)