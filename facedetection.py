# import cv2
# video_cap= cv2.VideoCapture(0)
# while True:
#     ret,video_data = video_cap.read()
#     cv2.imshow("video_live",video_data)
#     if cv2.waitkey(10) == ord("a"):
#         break
# video_cap.relese()

# this is only for open comra in system
###################################################

# import cv2

# video_cap = cv2.VideoCapture(0)
# paused = False                                          # Variable to track if the video is paused

# while True:
#     if not paused:
#         ret, video_data = video_cap.read()
#         if ret:
#             cv2.imshow("video_live", video_data)
    
#     key = cv2.waitKey(10)
    
#     if key == ord('q'):                                                         # Close the video and exit the loop when 'q' key is pressed
#         break
   

# # Release the video capture object and close all OpenCV windows
# video_cap.release()

#################################################################################=  now code for face detection3###################################
import cv2

face_cap=cv2.CascadeClassifier("c:/Users/dell/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0/LocalCache/local-packages/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)
paused = False                                         

while True:
    if not paused:
        ret, video_data = video_cap.read()
        col=cv2.CvtColor(video_data,cv2.COLOR_BGR2GRAY)
        if ret:
            cv2.imshow("video_live", video_data)
    
    key = cv2.waitKey(10)
    
    if key == ord('q'):                                                         
        break
   
video_cap.release()