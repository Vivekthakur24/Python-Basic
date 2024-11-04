import cv2
import mediapipe as mp

# Initialize MediaPipe Pose and Hands classes
mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose(static_image_mode=False, model_complexity=1, enable_segmentation=False, min_detection_confidence=0.5)
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

# Start webcam capture
cap = cv2.VideoCapture(0)

def count_fingers(hand_landmarks):
    """
    Count the number of fingers raised for a detected hand.
    A finger is considered raised if the tip is above the preceding joint.
    """
    # List of finger tip and corresponding PIP landmarks for comparison
    FINGER_TIPS = [8, 12, 16, 20]  # Index, middle, ring, and pinky fingers
    FINGER_PIP = [6, 10, 14, 18]  # PIP joint landmarks
    
    thumb_is_open = hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x  # Thumb rule

    fingers_open = [hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y 
                    for tip, pip in zip(FINGER_TIPS, FINGER_PIP)]

    return sum(fingers_open) + thumb_is_open  # Sum raised fingers

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to RGB for MediaPipe processing
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for pose and hand landmarks
    pose_result = pose.process(image_rgb)
    hands_result = hands.process(image_rgb)

    # Draw pose landmarks
    if pose_result.pose_landmarks:
        mp_drawing.draw_landmarks(frame, pose_result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Draw hand landmarks and count fingers
    if hands_result.multi_hand_landmarks:
        for hand_landmarks in hands_result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Count fingers and display the result on the frame
            fingers = count_fingers(hand_landmarks)
            cv2.putText(frame, f'Fingers: {fingers}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Pose and Finger Counting", frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
pose.close()
hands.close()
cv2.destroyAllWindows()


  # note
# please type pip install opencv-python mediapipe
# in terminal 