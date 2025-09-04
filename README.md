# HandTrackingProject

Control your system volume using simple hand gestures.  
This project detects the position of two fingers and adjusts the volume based on their distance — no physical contact with your device needed.

## Overview  

The application uses **MediaPipe** for hand tracking and **OpenCV-Python** for real-time video processing. By tracking the top points of two fingers, it calculates the distance between them and maps that distance to your system volume level.  

## Features  

- Real-time hand tracking  
- Gesture-based volume control (two-finger pinch/spread)  
- Built with Python  
- Visual feedback of the tracking process  

## Tech Stack  

- [Mediapipe](https://developers.google.com/mediapipe) – real-time hand tracking  
- [OpenCV-Python](https://opencv.org/) – image/video processing  

## Screenshots  

![ScreenShot](/images/htp2.png)  
![ScreenShot](/images/htp1.png)  
![ScreenShot](/images/htp3.png)  

## Demo  

🎥 [Watch the demo here](https://drive.google.com/drive/folders/1I2O3E5eSIasllyPGeNwzJ8mbwIrFinBG)

## How It Works  

1. The webcam feed is captured with OpenCV.  
2. MediaPipe detects and tracks the user’s hand landmarks in real time.  
3. The distance between two selected fingertips is calculated.  
4. This distance is mapped to system volume using a linear interpolation.  

