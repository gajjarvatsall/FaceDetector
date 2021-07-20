import cv2

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('/Users/vatsalgajjar/Downloads/haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
# img = cv2.imread('/Users/vatsalgajjar/Downloads/Paul walker.jpeg')

# To capture the video from webcam
webcam = cv2.VideoCapture(0)
# key = cv2.waitKey(1)

#  Iterrate forever over frames
while True:
    # Read the current frame
    successful_frame_read, frame = webcam.read()

    # Must convert into grayscale
    grayscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_image)

    # Draw rectangles around the faces
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x,y) , (x+w,y+h) , (0, 255, 0), 2)

    cv2.imshow('Face Detector',frame)
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key==81 or key==113:
        break


print("Code Completed") 