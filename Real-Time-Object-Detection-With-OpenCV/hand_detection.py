import cv2
import mediapipe as mp
from gemini import OCR
# from gpt_calls import gpt

cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Flag to indicate hand detection
hand_detected = False
consecutive_frames_without_detection = 0
photo_taken = True

api_key_abhy = "insert key here"
api_key = "insert key here"

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # Update hand_detected flag based on results
    if results.multi_hand_landmarks:
        print('hand detected')
        hand_detected = True
        photo_taken = False
        consecutive_frames_without_detection = 0
    else:
        if hand_detected:  # Only reset flag if it was previously True
            hand_detected = False
        consecutive_frames_without_detection += 1

        if consecutive_frames_without_detection > 200:
            if not photo_taken:
                # Take a photo
                cv2.imwrite("frame.jpg", img)
                print("ocring")
                # Process the photo
                # latex_content = gpt(api_key, "frame.jpg")
                latex_content = OCR("frame.jpg")
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

cap.release()