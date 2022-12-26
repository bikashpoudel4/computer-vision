import cv2

# Create a VideoCapture object
capture = cv2.VideoCapture(0)

# Create a window
cv2.namedWindow('frame')

# Create a button in the window
def take_photo(state, userdata):
    # Save the current frame to an image file
    cv2.imwrite('photo.jpg', frame)
    print('Photo saved!')

cv2.createButton('Take Photo', take_photo)

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    # Display the frame
    cv2.imshow('frame', frame)

    # Wait for a key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
capture.release()
cv2.destroyAllWindows()
