import streamlit as st
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

st.title("Video capture with OpenCV")

frame_placeholder = st.empty()

stop_button_pressed = st.button("Stop")

while cap.isOpened() and not stop_button_pressed:
    ret, frame = cap.read()

    if not ret:
        st.write("The video capture has ended!")
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame, channels="RGB")

cap.release()
cv2.destroyAllWindows()
