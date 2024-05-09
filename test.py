import streamlit as st
import cv2
import numpy as np

def takeImage():
    uploaded_file = st.file_uploader("Choose a image", type=['jpg', 'png'])

    if uploaded_file is not None:
        img = uploaded_file.read()
        if img:
            st.success("Image Uploaded Successfully")
        return img

st.header("Face Detection Model")
st.write("""Unlock the Faces: Discover the Hidden Expressions with Precision.""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    inp_img = takeImage()

    # storing image as a file
    if inp_img:
        with open("input.jpg", "wb") as f:
            f.write(inp_img)

with col2:
    st.write(
        """
        #### Image Entered
        """
    )
    st.image(inp_img)

image = cv2.imdecode(np.frombuffer(inp_img, np.uint8), cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.075,
    minNeighbors=5,
    minSize=(15, 15)
)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

for (x, y, w, h) in faces:
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = image[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

status = cv2.imencode('.jpg', image)[1].tobytes()
print("[INFO] Image besiktas2.jpg written to filesystem: ", status)

st.divider()

if len(faces) != 0:
    st.write(f"""### Output""")
    st.image(image, channels="BGR")
    st.write(f"""#### Information:""")
    if len(faces) > 1:
        st.write("Found {0} Faces in the image!".format(len(faces)))
    else:
        st.write("Found {0} Face in the image!".format(len(faces)))
else:
    st.write(f"""### Output""")
    st.write(
        f"Couldn't find any face in the image. Please enter any other image."
    )
