import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import imageio
from fer import FER
import numpy as np
import tensorflow as tf

class MoodDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mood Detection App")
        
        # Set up the GUI
        self.label = Label(root, text="Detecting Mood...", font=("Helvetica", 16))
        self.label.pack()
        
        # Set up the image panel
        self.image_label = Label(root)
        self.image_label.pack()
        
        # Initialize FER detector
        self.detector = FER()
        
        # Start video capture
        self.update_frame()
    
    def update_frame(self):
        # Capture video frame
        video_capture = imageio.get_reader('<video0>')
        frame = video_capture.get_next_data()

        # Convert to PIL Image
        image = Image.fromarray(frame)
        image = image.resize((640, 480))  # Resize image if needed

        # Convert image to array for emotion detection
        image_np = np.array(image)

        # Detect emotions
        emotions = self.detector.detect_emotions(image_np)
        if emotions:
            dominant_emotion = emotions[0]['emotions']
            max_emotion = max(dominant_emotion, key=dominant_emotion.get)
            suggestion = self.suggest_activity(max_emotion)
            self.label.config(text=f"Emotion: {max_emotion.capitalize()}\n{suggestion}")
        
        # Update the image display
        self.tk_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.tk_image)
        
        # Schedule the next frame update
        self.root.after(1000, self.update_frame)
    
    def suggest_activity(self, emotion):
        suggestions = {
            "happy": "Keep up the great mood! Consider going for a walk or sharing your happiness with friends.",
            "sad": "It's okay to feel sad. Try watching a favorite movie or talking to a friend.",
            "angry": "Take deep breaths or do some physical activity to release the tension.",
            "surprised": "Enjoy the moment! Maybe explore something new.",
            "neutral": "Why not try something new today or go for a short walk to refresh yourself?"
        }
        return suggestions.get(emotion, "Mood not recognized.")

# Create the Tkinter window
root = tk.Tk()
app = MoodDetectionApp(root)
root.mainloop()
