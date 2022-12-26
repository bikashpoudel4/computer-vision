import cv2

# Create a VideoCapture object
capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    # Flip the frame horizontally
    flipped_horizontally = cv2.flip(frame, 0)
    
    # "1" Flip around the y-axis (vertical flip)
    flipped_vertical = cv2.flip(frame, 1)
    
    # "-1" Flip around both the x-axis and y-axis (both horizontal and vertical flip)
    flipped_hv = cv2.flip(frame, -1)

    # Display the flipped frame
    cv2.imshow('horizontally', flipped_horizontally)
    cv2.imshow('y-axis (vertical flip)', flipped_vertical)
    cv2.imshow('horizontal and vertical', flipped_hv)

    # Wait for a key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
capture.release()
cv2.destroyAllWindows()
