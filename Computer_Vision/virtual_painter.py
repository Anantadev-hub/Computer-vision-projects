import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

# Create a blank canvas
canvas = None

# Previous point
prev_x = None
prev_y = None

# Blue color range in HSV
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Flip the frame so it behaves like a mirror
    frame = cv2.flip(frame, 1)

    # Create canvas only once
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Convert frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Detect blue
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Remove small noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:
        # Largest blue object
        c = max(contours, key=cv2.contourArea)

        # Ignore tiny objects
        if cv2.contourArea(c) > 500:

            M = cv2.moments(c)

            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # Show tracking point
                cv2.circle(frame, (cx, cy), 10, (0, 255, 0), -1)

                # Draw if previous point exists
                if prev_x is not None:
                    cv2.line(
                        canvas,
                        (prev_x, prev_y),
                        (cx, cy),
                        (255, 0, 0),
                        5
                    )

                prev_x = cx
                prev_y = cy

    else:
        # Stop drawing when object disappears
        prev_x = None
        prev_y = None

    # Combine webcam and drawing
    result = cv2.add(frame, canvas)

    cv2.putText(
        result,
        "Press C to Clear | Q to Quit",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.imshow("Virtual Painter", result)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("c"):
        canvas = np.zeros_like(frame)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()