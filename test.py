import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
import numpy as np

class FaceDetector(VideoTransformerBase):
    def transform(self, frame):
        # Convert the frame to BGR format
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Load the Haar cascade for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Convert the frame back to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        return frame

def main():
    st.title("Webcam Face Detection")

    run = st.checkbox("Run")

    webrtc_ctx = webrtc_streamer(
        key="example",
        video_transformer_factory=FaceDetector,
        async_transform=False,
        use_webcam=True,
    )

    if not run:
        st.write('Stopped')

if __name__ == "__main__":
    main()
