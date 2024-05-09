import streamlit as st
from streamlit_webrtc import webrtc_streamer

def main():
    st.title("Webcam Live Feed")
    run = st.checkbox('Run')

    webrtc_ctx = webrtc_streamer(key="example", video_transformer_factory=None, async_transform=False)

    if webrtc_ctx.video_transformer:
        st.write('Stopped')

if __name__ == "__main__":
    main()
