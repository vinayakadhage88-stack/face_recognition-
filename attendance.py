import cv2
import face_recognition
import pickle
import csv
from datetime import datetime
import os

# Load encodings
with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

# Create attendance folder
if not os.path.exists("attendance"):
    os.makedirs("attendance")

today = datetime.now().strftime("%Y-%m-%d")
attendance_file = f"attendance/{today}.csv"

marked_names = set()

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for faster processing
    small = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)

    for encoding, box in zip(encodings, boxes):
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"

        if True in matches:
            index = matches.index(True)
            name = data["names"][index]

            if name not in marked_names:
                marked_names.add(name)
                with open(attendance_file, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([name, datetime.now().strftime("%H:%M:%S")])

        # scale box back
        top, right, bottom, left = [v * 2 for v in box]

        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(frame, name, (left, top-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

    cv2.imshow("Attendance", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
