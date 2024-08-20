import cv2 # Importing the OpenCV library, which is used for real-time computer vision.
import cvzone # Importing the cvzone library, which provides additional functionalities for computer vision tasks.
from cvzone.HandTrackingModule import HandDetector # Importing the HandDetector class from the cvzone HandTrackingModule.
import mediapipe # Importing the mediapipe library, which is used for real-time machine learning and computer vision tasks.
import random
import time

cap = cv2.VideoCapture(0)  # Initializing a VideoCapture object and setting the video source to 0 (usually the default webcam).
cap.set(3,640) # Setting the width of the frames to 640.
cap.set(4,480) # Setting the height of the frames to 480.

detector = HandDetector(maxHands=1) # Initializing a HandDetector object with a maximum of 1 hand to be detected.

timer = 0 # Initializing a timer variable to keep track of time.
stateResult = False # Initializing a stateResult variable to keep track of the game state.
startGame = False # Initializing a startGame variable to keep track of the game state.
scores = [0,0] # Initializing a scores list to keep track of the scores for the AI and the player.

while True:
    ret, img = cap.read() # Reading a frame from the video source.

    imBG = cv2.imread("Resources/BG.png") # Reading the background image.
    imgScaled = cv2.resize(img,(0,0),None,0.875,0.875) # Resizing the frame to 87.5% of its original size.
    imgScaled = imgScaled[:,80:480] # Cropping the frame to remove the leftmost 80 pixels and the rightmost pixels beyond 480.

    # Finding hands in the frame.
    hands, img = detector.findHands(imgScaled,draw=True)

    if startGame: # If the game has started.

        if stateResult is False : # If the game state is not yet determined.
            timer = time.time() - initialTime # Calculating the time elapsed since the game started.
            cv2.putText(imBG,str(int(timer)),(605,435),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),4) # Displaying the time elapsed on the frame.
        if timer>3: # If the time elapsed is greater than 3 seconds.
            stateResult = True # Setting the game state to determined.
            timer = 0 # Resetting the timer.

            if hands: # If hands are detected.
                hand = hands[0] # Getting the first hand detected.
                fingers= detector.fingersUp(hand) # Getting the fingers up of the hand.
                print(fingers) # Printing the fingers up of the hand.
                if fingers == [0,0,0,0,0]: # If the fingers up are [0,0,0,0,0].
                    playermove = 1 # Setting the player move to 1 (rock).
                if fingers == [1,1,1,1,1]: # If the fingers up are [1,1,1,1,1].
                    playermove = 2 # Setting the player move to 2 (paper).
                if fingers == [0,1,1,0,0]: # If the fingers up are [0,1,1,0,0].
                    playermove = 3 # Setting the player move to 3 (scissors).
                
                randomNumber = random.randint(1,3) # Generating a random number between 1 and 3.
                imgAI = cv2.imread(f"Resources/{randomNumber}.png",cv2.IMREAD_UNCHANGED) # Reading the AI image based on the random number.
                imBG = cvzone.overlayPNG(imBG,imgAI,(149,310)) # Overlaying the AI image on the background image.
                
                # Player Wins
                if (playermove == 1 and randomNumber == 3) or \
                    (playermove == 2 and randomNumber == 1) or \
                    (playermove == 3 and randomNumber == 2): # If the player move is scissors and the AI move is paper.
                        scores[1] += 1 # Incrementing the player score.
 
                # AI Wins
                if (playermove == 3 and randomNumber == 1) or \
                    (playermove == 1 and randomNumber == 2) or \
                    (playermove == 2 and randomNumber == 3): # If the player move is paper and the AI move is scissors.
                        scores[0] += 1 # Incrementing the AI score.

                # print(playermove)

    imBG[234:654,795:1195] = imgScaled # Replacing a section of the background image with the processed frame.

    if stateResult: # If the game state is determined.
        imBG = cvzone.overlayPNG(imBG,imgAI,(149,310)) # Overlaying the AI image on the background image.

    cv2.putText(imBG,str(scores[0]),(410,215),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),6) # Displaying the AI score on the frame.
    cv2.putText(imBG,str(scores[1]),(1112,215),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),6) # Displaying the player score on the frame.


    if not ret: # If the frame was not successfully read.
        print("Failed to grab a frame")
        break

    # cv2.imshow("video_live", img) # Displaying the processed frame.
    cv2.imshow("ROCK PAPER SCISSOR",imBG) # Displaying the background image with the processed frame.
    # cv2.imshow("Scaled",imgScaled) # Displaying the cropped and resized frame.

    key = cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        initialTime  = time.time()
        stateResult = False

    if cv2.waitKey(10) == ord("a"):
        break


cap.release()
cv2.destroyAllWindows()