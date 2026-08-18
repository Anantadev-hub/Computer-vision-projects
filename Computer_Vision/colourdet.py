import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

# Blue color range in HSV
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

# Green color range in HSV
lower_green = np.array([35,100,50])
upper_green = np.array([85,255,255])

# Yellow color range in HSV
lower_yellow= np.array([20,100,100])
upper_yellow = np.array([35,255,255])

#Black colour range in HSV
lower_black = np.array([0,0,0])
upper_black = np.array([180,255,52])

#Red Colour range in HSV
lower_red1=np.array([159,50,70])
upper_red1=np.array([180,250,100])
lower_red2=np.array([0,50,70])
upper_red2=np.array([9,255,200])
while True:
    # Capture frame
    ret, frame = cap.read()

    if not ret:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert BGR image to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask that only keeps blue colors
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_green, upper_green)
    mask3 = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask4 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask5 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask6 = cv2.inRange(hsv, lower_black, upper_black)

    # Remove small noise
    kernel = np.ones((5, 5), np.uint8)
    mask1 = cv2.erode(mask1, kernel, iterations=1)
    mask1 = cv2.dilate(mask1, kernel, iterations=2)
    mask2 = cv2.erode(mask2, kernel, iterations=1)
    mask2 = cv2.dilate(mask2, kernel, iterations=2)
    mask3 = cv2.dilate(mask3, kernel, iterations=2)
    mask3 = cv2.erode(mask3, kernel, iterations=1)
    mask4 = cv2.erode(mask4, kernel, iterations=1)
    mask4 = cv2.dilate(mask4, kernel, iterations=2)
    mask5 =cv2.erode(mask5, kernel, iterations=1)
    mask5 = cv2.dilate(mask5, kernel, iterations=2)
    mask6 = cv2.erode(mask6, kernel, iterations=1)
    mask6 = cv2.dilate(mask6, kernel, iterations=2)

    #Find contours of Red1 objects
    contours, _ = cv2.findContours(
        mask4,
        cv2.RETR_EXTERNAL, #Find the outer boundary of each object and represent that boundary using only the necessary points
        cv2.CHAIN_APPROX_SIMPLE

    )
    #Loop through all detected red1 objects
    for contour in contours:
        if cv2.contourArea(contour) > 500: #ignore very small objects
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(
                frame,
                (x,y),
                (x+w, y+ h),
                (0, 255, 0),
                2
            )
            # Calculate centre
            cx = x + w // 2
            cy = y + h // 2
            # Draw Centre point
            cv2.circle(
                frame,
                (cx, cy),
                5,
                (0, 0, 255),
                -1

            )

            #Display colour name
            cv2.putText(
                frame,
                "RED",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255,0,0),
                2,
            )
            #Display coordinates
            cv2.putText(
                frame,
                f"X:{cx}  Y:{cy}",
                (x, y + h + 25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255,255,255),
                2,
            )
    #Find contours of Red1 objects
    contours, _ = cv2.findContours(
        mask5,
        cv2.RETR_EXTERNAL, #Find the outer boundary of each object and represent that boundary using only the necessary points
        cv2.CHAIN_APPROX_SIMPLE

    )
    for contour in contours:
        if cv2.contourArea(contour) > 500: #ignore very small objects
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(
                frame,
                (x,y),
                (x+w, y+ h),
                (0, 255, 0),
                2
            )
            # Calculate centre
            cx = x + w // 2
            cy = y + h // 2
            # Draw Centre point
            cv2.circle(
                frame,
                (cx, cy),
                5,
                (0, 0, 255),
                -1

            )

            #Display colour name
            cv2.putText(
                frame,
                "RED",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255,0,0),
                2,
            )
            #Display coordinates
            cv2.putText(
                frame,
                f"X:{cx}  Y:{cy}",
                (x, y + h + 25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255,255,255),
                2,
            )

    # Find contours of blue objects
    contours, _ = cv2.findContours(
        mask1,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Loop through all detected blue objects
    for contour in contours:

        # Ignore very small objects
        if cv2.contourArea(contour) > 500:

            # Get bounding rectangle
            x, y, w, h = cv2.boundingRect(contour)

            # Draw rectangle
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Calculate center
            cx = x + w // 2
            cy = y + h // 2

            # Draw center point
            cv2.circle(
                frame,
                (cx, cy),
                5,
                (0, 0, 255),
                -1
            )

            # Display color name
            cv2.putText(
                frame,
                "BLUE",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2
            )

            # Display coordinates
            cv2.putText(
                frame,
                f"X:{cx}  Y:{cy}",
                (x, y + h + 25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2
            )
    # Loop through all detected yellow objects
    contours, _ = cv2.findContours(
        mask3,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    for contour in contours:

        # Ignore very small objects
        if cv2.contourArea(contour) > 500:

            # Get bounding rectangle
            x, y, w, h = cv2.boundingRect(contour)

            # Draw rectangle
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Calculate center
            cx = x + w // 2
            cy = y + h // 2

            # Draw center point
            cv2.circle(
                frame,
                (cx, cy),
                5,
                (0, 0, 255),
                -1
            )

            # Display color name
            cv2.putText(
                frame,
                "Yellow",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2
            )

            # Display coordinates
            cv2.putText(
                frame,
                f"X:{cx}  Y:{cy}",
                (x, y + h + 25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2
            )

    # Find contours of green objects
    contours, _ = cv2.findContours(
         mask2,
         cv2.RETR_EXTERNAL,
         cv2.CHAIN_APPROX_SIMPLE
    )

    # Loop through all detected green objects
    for contour in contours:

        # Ignore very small objects
        if cv2.contourArea(contour) > 500:
            # Get bounding rectangle
            x, y, w, h = cv2.boundingRect(contour)

                # Draw rectangle
            cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (255, 0, 0),
                    2
                )

            # Calculate center
            cx = x + w // 2
            cy = y + h // 2

                # Draw center point
            cv2.circle(
             frame,
             (cx, cy),
             5,
             (0, 0, 255),
                -1
             )

                # Display color name
            cv2.putText(
                frame,
                "GREEN",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2
            )

                # Display coordinates
            cv2.putText(
                frame,
                f"X:{cx}  Y:{cy}",
                (x, y + h + 25),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2
            )

    # Show webcam
    cv2.imshow("Color Detector", frame)

    # Show mask
    cv2.imshow("Mask1", mask1)
    cv2.imshow("Mask2", mask2)
    cv2.imshow("Mask3", mask3)

    # Quit when Q is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
     break

# Release webcam
cap.release()
cv2.destroyAllWindows()