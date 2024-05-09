from utils.graphing import plot # importing from utils folder

import cv2 # compvis library
import math # self explanitory
import mediapipe as mp # for recognizing hands
mp_drawing = mp.solutions.drawing_utils # setups
mp_hands = mp.solutions.hands

def executable(camera):
    xCoords = [] # current x-coords of hand
    yCoords = [] # current y-coords of hand

    hand_classification_dict = { # changes the number value to its name
        0: "WRIST",
        1: "THUMB_CMC",
        2: "THUMB_MPC",
        3: "THUMB_IP",
        4: "THUMB_TIP",
        5: "INDEX_FINGER_MCP",
        6: "INDEX_FINGER_PIP",
        7: "INDEX_FINGER_DIP",
        8: "INDEX_FINGER_TIP",
        9: "MIDDLE_FINGER_MCP",
        10: "MIDDLE_FINGER_PIP",
        11: "MIDDLE_FINGER_DIP",
        12: "MIDDLE_FINGER_TIP",
        13: "RING_FINGER_MCP",
        14: "RING_FINGER_PIP",
        15: "RING_FINGER_DIP",
        16: "RING_FINGER_TIP",
        17: "PINKY_FINGER_MCP",
        18: "PINKY_FINGER_PIP",
        19: "PINKY_FINGER_DIP",
        20: "RING_FINGER_TIP"
    }

    cap = cv2.VideoCapture(camera) # start capture through camera
    with (
        mp_hands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)
        as hands
    ):
      while cap.isOpened():
        success, image = cap.read()
        if not success:
          print("Empty Camera Frame (no success).")
          continue

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB) # flip camera so its mirrored
        # mark the image as not writeable to pass by reference (if performance issues)
        image.flags.writeable = False
        results = hands.process(image)
        image_height, image_width, _ = image.shape
        # Draw the hand annotations on the image
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
          for hand_landmarks in results.multi_hand_landmarks:
            xCoords = [] # cleans them for another update
            yCoords = []
            # Gets all point location coords
            print(math.floor(hand_landmarks.landmark[0].x * image_width))
            for ids, landmrk in enumerate(hand_landmarks.landmark):
                # print(ids, landmrk)
                cx, cy = landmrk.x * image_width, landmrk.y*image_height
                print(hand_classification_dict[ids], cx, cy) # could comment out
                # print (ids, cx, cy)
                xCoords.append(cx)
                yCoords.append(cy)

            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.imshow('Registering Hands', image) # Window Name, stream(image)
        if cv2.waitKey(5) & 0xFF == 27: # `ESC` key
          break
    cap.release()
    plot(xCoords, yCoords) # prints final
