import cv2
import numpy as np
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['fridgeminder_pro']  # Connect to the 'fridgeminder_pro' database
collection = db['detected_items']  # Collection to store detected items

# Initialize OpenCV
cap = cv2.VideoCapture(0)

# Define color ranges for object detection
lower_g1 = np.array([35, 100, 100])
upper_g1 = np.array([85, 255, 255])

lower_o1 = np.array([5, 150, 150])
upper_o1 = np.array([15, 255, 255])

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        ret, frame = cap.read()
        
        if ret:
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Mask for Green (e.g., Green Apple) and Orange (e.g., Carrot)
            g1_mask = cv2.inRange(hsv_frame, lower_g1, upper_g1)
            o1_mask = cv2.inRange(hsv_frame, lower_o1, upper_o1)

            # Result of masked areas
            g1_result = cv2.bitwise_and(frame, frame, mask=g1_mask)
            o1_result = cv2.bitwise_and(frame, frame, mask=o1_mask)

            # Detect Green Apple
            g1_contours, _ = cv2.findContours(g1_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in g1_contours:
                if cv2.contourArea(contour) > 100:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame, "Green Apple", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    
                    # Log detection to MongoDB
                    detection_data = {
                        "item": "Green Apple",
                        "timestamp": datetime.now(),
                        "location": {"x": x, "y": y, "width": w, "height": h}
                    }
                    collection.insert_one(detection_data)  # Save detection data to MongoDB
                    print("Green Apple detected and saved to database.")

            # Detect Carrot
            o1_contours, _ = cv2.findContours(o1_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in o1_contours:
                if cv2.contourArea(contour) > 100:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 165, 255), 2)
                    cv2.putText(frame, "Carrot", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 165, 255), 2)
                    
                    # Log detection to MongoDB
                    detection_data = {
                        "item": "Carrot",
                        "timestamp": datetime.now(),
                        "location": {"x": x, "y": y, "width": w, "height": h}
                    }
                    collection.insert_one(detection_data)  # Save detection data to MongoDB
                    print("Carrot detected and saved to database.")

            # Show Frames
            cv2.imshow("Original Frame", frame)
            cv2.imshow("Detected Green Objects", g1_result)
            cv2.imshow("Detected Carrots", o1_result)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Error: Could not read frame.")
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()