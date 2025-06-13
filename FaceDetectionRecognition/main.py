import cv2
import os
import numpy as np
import face_recognition

# Load known faces
def load_known_faces(dataset_path='dataset'):
    known_encodings = []
    known_names = []

    for filename in os.listdir(dataset_path):
        if filename.lower().endswith(('.jpg', '.png', '.jpeg')):
            name = os.path.splitext(filename)[0]
            image_path = os.path.join(dataset_path, filename)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(name)
            else:
                print(f"[Warning] No face found in {filename}")
    return known_encodings, known_names

# Main app loop
def run_app():
    known_encodings, known_names = load_known_faces()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[Error] Cannot access webcam")
        return

    print("[INFO] Starting webcam...")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]  # BGR to RGB

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            name = "Unknown"
            distances = face_recognition.face_distance(known_encodings, face_encoding)
            if len(distances) > 0:
                best_match_index = np.argmin(distances)
                if distances[best_match_index] < 0.6:
                    name = known_names[best_match_index]

            # Scale back up to original frame size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw rectangle and label
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        cv2.imshow("Face Detection and Recognition", frame)

        key = cv2.waitKey(1)
        if key == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_app()
