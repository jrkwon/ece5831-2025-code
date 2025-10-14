import cv2

# Create a VideoCapture object (0 for default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # If frame reading was unsuccessful, break the loop
    if not ret:
        print("Failed to grab frame.")
        break

    # Display the captured frame
    cv2.imshow('Camera Feed', frame)

    # Wait for 1 millisecond for a key press. If 'q' is pressed, exit.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
cap.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()