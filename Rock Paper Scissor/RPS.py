import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import mediapipe 
import time
import random

cap = cv2.VideoCapture(0)  # Change 0 to your video source
cap.set(3,640)
cap.set(4,480)

detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
startGame = False
scores = [0,0] # [AI , Player]


while True:
    ret, img = cap.read()

    imBG = cv2.imread("Resources/BG.png")
    imgScaled = cv2.resize(img,(0,0),None,0.875,0.875)
    imgScaled = imgScaled[:,80:480]

    #find hands
    hands , img = detector.findHands(imgScaled,draw=True)

    if startGame:

        if stateResult is False :
            timer = time.time() - initialTime
            cv2.putText(imBG,str(int(timer)),(605,435),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),4)
        if timer>3:
            stateResult = True
            timer = 0

            if hands:
                hand = hands[0]
                fingers= detector.fingersUp(hand)
                print(fingers)
                if fingers == [0,0,0,0,0]:
                    playermove = 1
                if fingers == [1,1,1,1,1]:
                    playermove = 2
                if fingers == [0,1,1,0,0]:
                    playermove = 3
                
                randomNumber = random.randint(1,3)
                imgAI = cv2.imread(f"Resources/{randomNumber}.png",cv2.IMREAD_UNCHANGED)
                imBG = cvzone.overlayPNG(imBG,imgAI,(149,310))
                
                # Player Wins
                if (playermove == 1 and randomNumber == 3) or \
                    (playermove == 2 and randomNumber == 1) or \
                    (playermove == 3 and randomNumber == 2):
                        scores[1] += 1
 
                # AI Wins
                if (playermove == 3 and randomNumber == 1) or \
                    (playermove == 1 and randomNumber == 2) or \
                    (playermove == 2 and randomNumber == 3):
                        scores[0] += 1

                # print(playermove)

    imBG[234:654,795:1195] = imgScaled

    if stateResult:
        imBG = cvzone.overlayPNG(imBG,imgAI,(149,310))

    cv2.putText(imBG,str(scores[0]),(410,215),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),6)
    cv2.putText(imBG,str(scores[1]),(1112,215),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),6)


    if not ret:
        print("Failed to grab a frame")
        break

    # cv2.imshow("video_live", img)
    cv2.imshow("ROCK PAPER SCISSOR",imBG)
    # cv2.imshow("Scaled",imgScaled)



    key = cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        initialTime  = time.time()
        stateResult = False

    if cv2.waitKey(10) == ord("a"):
        break


cap.release()
cv2.destroyAllWindows()

