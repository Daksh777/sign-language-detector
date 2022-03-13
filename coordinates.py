import cv2

def click_event(event, x, y, flags, params):

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:

        # displaying the coordinates on the terminal
        print(f"Coordinates: {x}, {y}")

    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:

        # displaying the coordinates on the terminal
        print(x, y)