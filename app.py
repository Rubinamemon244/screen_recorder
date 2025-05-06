from fileinput import filename
import streamlit as st  # type: ignore
import pyautogui # type: ignore
import cv2 # type: ignore
import numpy as np # type: ignore
import time
import os
st.set_page_config(page_title="Screen recorder", layout="centered")
st.title("🎥Screen Recorder - Python + Streamlit")

filename = st.text_input("Enter the filename", "recording.mp4")

duration = st.slider("Select the duration (second)", 10, 36000, 20)
fps = st.slider("Select the frames rate (FPS)", 1, 60, 30)

if st.button("Start Recording"):
    st.success("Recording...")

    screen_size = pyautogui.size()
    codec = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(filename, codec, fps, screen_size)

    start_time = time.time()
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) 

        out.write(frame)

        if time.time() - start_time > duration:
            break

    out.release()
    st.success(f"Recording saved as {filename}.")

    with open(filename, "rb") as video_file:
     st.download_button(
        label="📥 Download Recording",
        data=video_file,
        file_name=filename,
    )

# REMOVE or comment out deletion here:
# os.remove(filename)

    if st.button("🗑️ Delete Recording from Server"):
        st.success("Recording deleted from server.")

        os.remove(filename)