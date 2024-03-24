import cv2
import mediapipe as mp
from gemini import OCR
import os
from dotenv import load_dotenv
from imutils.video import VideoStream
# from gpt_calls import gpt

def HandDetection(video_path):

    GEMINI_API_KEY = os.getenv("GEMINI_KEY")

    #cap = cv2.VideoCapture(video_path)
    vs = VideoStream(src=video_path).start()

    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    # Flag to indicate hand detection
    hand_detected = False
    consecutive_frames_without_detection = 0
    consecutive_frames_with_detection = 0
    photo_taken = True

    # api_key_abhy = "insert key here"
    api_key = GEMINI_API_KEY

    final_latex = r'''\documentclass{article}

    % Packages
    \usepackage[utf8]{inputenc} % UTF-8 encoding
    \usepackage[T1]{fontenc} % Font encoding
    \usepackage{lipsum} % For generating dummy text, can be removed

    \begin{document}

    '''

    while True:
        img = vs.read()

        if img is None:
            break

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        # Update hand_detected flag based on results
        if results.multi_hand_landmarks:
            #print('hand detected')
            photo_taken = False
            consecutive_frames_without_detection = 0
            consecutive_frames_with_detection += 1

        else:
            consecutive_frames_with_detection = 0
            if hand_detected:  # Only reset flag if it was previously True
                hand_detected = False
            consecutive_frames_without_detection += 1

            if consecutive_frames_without_detection > 20:
                if not photo_taken:
                    # Take a photo
                    cv2.imwrite("frame.jpg", img)
                    print("ocring")
                    # Process the photo
                    # latex_content = gpt(api_key, "frame.jpg")
                    latex_content = OCR(api_key, "frame.jpg")
                    final_latex += latex_content
                    print(latex_content)
                    photo_taken = True
                    consecutive_frames_without_detection = 0

        # Process and display image based on hand detection
        if hand_detected:
            for handlandmark in results.multi_hand_landmarks:
                for id, lm in enumerate(handlandmark.landmark):
                    h, w, _ = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx, cy), 4, (0, 0, 255), cv2.FILLED)

                mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    vs.stop()

    final_latex += r'''

    \end{document}'''

    return final_latex