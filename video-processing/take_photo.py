import cv2

# Create a VideoCapture object
capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    # Display the frame
    cv2.imshow('frame', frame)

    # Wait for a key press
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('p'):
        # Save the frame to an image file
        cv2.imwrite('photo.jpg', frame)
        print('Photo saved!')

# When everything is done, release the capture
capture.release()
cv2.destroyAllWindows()
