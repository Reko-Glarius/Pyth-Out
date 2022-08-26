import mediapipe as mp 
import numpy as np 
import cv2
import pyautogui
import pydirectinput

# import utils

# UP - Levantar Guardia (Defenderse)
# X - Gancho Derecho    (Golpe)
# S - Gancho Izquierdo  (Golpe)
# Z - Golpe al Higado   (Especial)

# TODO: 
# LEFT  - 
# RIGHT - 

button_switch = -1
is_press = False

width = 1920
height = 1080

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)

with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # image = cv2.flip(image, 1)
        result = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        mp_drawing.draw_landmarks(
        image,
        result.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        try:
            if(result.pose_landmarks.landmark[16].x < result.pose_landmarks.landmark[14].x and result.pose_landmarks.landmark[16].visibility>0.7):
                if(is_press):
                    pass
                else:
                    print("Press X")
                    pydirectinput.keyDown("x")
                    button_switch = 0
                    is_press = True
            elif(result.pose_landmarks.landmark[15].x > result.pose_landmarks.landmark[13].x and result.pose_landmarks.landmark[15].visibility>0.7):
                if(is_press):
                    pass
                else:
                    print("Press S")
                    pydirectinput.keyDown("s")
                    button_switch = 1
                    is_press = True
            elif(result.pose_landmarks.landmark[16].x > result.pose_landmarks.landmark[15].x 
                    and result.pose_landmarks.landmark[15].visibility>0.7
                    and result.pose_landmarks.landmark[15].visibility>0.7):
                if(is_press):
                    pass
                else:
                    print("Press Z")
                    pydirectinput.keyDown("z")
                    button_switch = 2
                    is_press = True
            elif(result.pose_landmarks.landmark[15].y*width < result.pose_landmarks.landmark[2].y*width or 
                    result.pose_landmarks.landmark[16].y*width < result.pose_landmarks.landmark[5].y*width):
                if(is_press):
                    pass
                else:
                    print("Press UP")
                    pydirectinput.keyDown("up")
                    button_switch = 3
                    is_press = True

            else:
                if(button_switch == 0):
                    print("Des-Press X")
                    is_press = False
                    button_switch = -1
                    pydirectinput.keyUp("x")

                elif(button_switch == 1):
                    print("Des-Press S")
                    is_press = False
                    button_switch = -1
                    pydirectinput.keyUp("s")

                elif(button_switch == 2):
                    print("Des-Press Z")
                    is_press = False
                    button_switch = -1
                    pydirectinput.keyUp("z")

                elif(button_switch == 3):
                    print("Des-Press UP")
                    is_press = False
                    button_switch = -1
                    pydirectinput.keyUp("up")

        except:
            continue
        
        image = cv2.flip(image, 1)
        cv2.imshow("image", image)

        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            cap.release()
            break