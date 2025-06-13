# 👤 Face Detection and Recognition App

This project is a real-time **face detection and recognition** application built with Python, OpenCV, and the `face_recognition` library. It captures video from your webcam, detects faces in the frame, and identifies them using preloaded face images from a dataset folder.

---

## 🧠 Features

- Real-time webcam access using OpenCV
- Face detection and face encoding using `face_recognition`
- Matches detected faces with known images from the `dataset/` folder
- Displays bounding boxes and names for recognized faces
- Labels unknown faces gracefully
- Warns about images without detectable faces during dataset loading

---

## 🛠️ Requirements

Make sure you have the following Python packages installed:

```bash
pip install opencv-python face_recognition numpy
```

## ▶️ How to Run
1. **Add known faces:**

- Put clear face images in the dataset/ folder.

- Each file should be named as the person's name (e.g., john.jpg).

2. **Run the app:**

```bash
python app.py
```
3. **Usage:**

- The webcam window will open.

- Recognized faces will be labeled.

- Press ESC key to close the window and stop the app.

## 👨‍💻 Author
### Made with 💻 by [Satya Mehta](https://github.com/satya-mehta)