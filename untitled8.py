import cv2
from deepface import DeepFace

# Define a function to suggest activities based on the detected emotion
def suggest_activity(emotion):
    suggestions = {
        "happy": "Keep up the great mood! Consider going for a walk or sharing your happiness with friends.",
        "sad": "It's okay to feel sad. Try watching a favorite movie or talking to a friend.",
        "angry": "Take deep breaths or do some physical activity to release the tension.",
        "surprised": "Enjoy the moment! Maybe explore something new.",
        "neutral": "Why not try something new today or go for a short walk to refresh yourself?"
    }
    return suggestions.get(emotion, "Mood not recognized.")

# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect emotion
    try:
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = analysis[0]['dominant_emotion']
        activity_suggestion = suggest_activity(emotion)

        # Display the emotion on the frame
        cv2.putText(frame, f'Emotion: {emotion}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, activity_suggestion, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    except Exception as e:
        print(f"Error: {e}")

    # Show the frame with the detected emotion
    cv2.imshow('Mood Detection', frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
