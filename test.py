import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import numpy as np

# Function to detect faces in a frame
def detect_faces(frame):
    # Load the pre-trained Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return frame

# Streamlit UI
st.title("Real-Time Face Detection")

# Stream the webcam feed
webrtc_ctx = webrtc_streamer(key="example", video_transformer_factory=detect_faces)
