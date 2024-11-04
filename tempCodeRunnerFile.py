import cv2

video_cap = cv2.VideoCapture(0)
paused = False  # Variable to track if the video is paused

while True:
    if not paused:
        ret, video_data = video_cap.read()
        if ret:
            cv2.imshow("video_live", video_data)
    
    key = cv2.waitKey(10)
    
    if key == ord('q'):  # Close the video and exit the loop when 'q' key is pressed
        break
   

# Release the video capture object and close all OpenCV windows
video_cap.release()
cv2.destroyAllWindows()