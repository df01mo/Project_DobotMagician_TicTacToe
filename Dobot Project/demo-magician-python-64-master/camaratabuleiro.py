import numpy as np
import cv2

cap = cv2.VideoCapture(1)

# Minimum and maximum area thresholds for object filtering
min_area = 500
max_area = 5000

# Kernel for morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (45, 45))

# Array to store previous object positions
prev_positions = []

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])

    mask = cv2.inRange(hsv, low_green, high_green)

    # Perform morphological operations to remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    object_detected = False
    for contour in contours:
        # Calculate the position of the object
        x, y, w, h = cv2.boundingRect(contour)
        centroid_x = x + (w // 2)
        centroid_y = y + (h // 2)

        # Calculate the area of the contour
        area = cv2.contourArea(contour)

        if min_area <= area <= max_area:
            # Draw a bounding rectangle around the object
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Draw a small circle at the centroid
            cv2.circle(frame, (centroid_x, centroid_y), 2, (0, 255, 0), -1)

            # Determine the position number based on the centroid coordinates
            position = 0
            if centroid_x < width / 3:
                if centroid_y < height / 3:
                    position = 1
                elif centroid_y < 2 * height / 3:
                    position = 4
                else:
                    position = 7
            elif centroid_x < 2 * width / 3:
                if centroid_y < height / 3:
                    position = 2
                elif centroid_y < 2 * height / 3:
                    position = 5
                else:
                    position = 8
            else:
                if centroid_y < height / 3:
                    position = 3
                elif centroid_y < 2 * height / 3:
                    position = 6
                else:
                    position = 9

            if position != 0 and position not in prev_positions:
                object_detected = True
                prev_positions.append(position)
                print("Object detected at position:", position)
                break
            
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == 13:  # Check if Enter key is pressed
        prev_positions = []

cap.release()
cv2.destroyAllWindows()








