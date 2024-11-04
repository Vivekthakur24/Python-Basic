import cv2
import mediapipe as mp

# Initialize MediaPipe Pose class with optional model complexity
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, model_complexity=1, enable_segmentation=False, min_detection_confidence=0.5)

# Initialize drawing utility for landmarks
mp_drawing = mp.solutions.drawing_utils

# Read image or use webcam
cap = cv2.VideoCapture(0)  # Use 0 for webcam

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Convert the frame to RGB (MediaPipe uses RGB)
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the image for pose landmarks
    result = pose.process(image_rgb)
    
    # Draw pose landmarks if confidence is sufficient
    if result.pose_landmarks:
        mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    # Show the result
    cv2.imshow("Pose Estimation", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
pose.close()  # Close the pose object to free resources
cv2.destroyAllWindows()




# note
# please type pip install opencv-python mediapipe
# in terminal 