# from fileinput import filename
# import streamlit as st  # type: ignore
# import pyautogui # type: ignore
# import cv2 # type: ignore
# import numpy as np # type: ignore
# import time
# import os
# st.set_page_config(page_title="Screen recorder", layout="centered")
# st.title("🎥Screen Recorder - Python + Streamlit")

# filename = st.text_input("Enter the filename", "recording.mp4")

# duration = st.slider("Select the duration (second)", 10, 36000, 20)
# fps = st.slider("Select the frames rate (FPS)", 1, 60, 30)

# if st.button("Start Recording"):
#     st.success("Recording...")

#     screen_size = pyautogui.size()
#     codec = cv2.VideoWriter_fourcc(*"mp4v")
#     out = cv2.VideoWriter(filename, codec, fps, screen_size)

#     start_time = time.time()
#     while True:
#         img = pyautogui.screenshot()
#         frame = np.array(img)
#         frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) 

#         out.write(frame)

#         if time.time() - start_time > duration:
#             break

#     out.release()
#     st.success(f"Recording saved as {filename}.")

#     with open(filename, "rb") as video_file:
#      st.download_button(
#         label="📥 Download Recording",
#         data=video_file,
#         file_name=filename,
#     )

# # REMOVE or comment out deletion here:
# # os.remove(filename)

#     if st.button("🗑️ Delete Recording from Server"):
#         st.success("Recording deleted from server.")

#         os.remove(filename)

# import streamlit as st  # type: ignore
# import cv2  # type: ignore
# import numpy as np  # type: ignore
# import time
# import os
# from mss import mss  # type: ignore

# st.set_page_config(page_title="Screen recorder", layout="centered")
# st.title("🎥 Screen Recorder - Python + Streamlit")

# filename = st.text_input("Enter the filename", "recording.mp4")
# duration = st.slider("Select the duration (seconds)", 10, 36000, 20)
# fps = st.slider("Select the frame rate (FPS)", 1, 60, 30)

# if st.button("Start Recording"):
#     st.success("Recording...")

#     with mss() as sct:
#         monitor = sct.monitors[1]  # Full screen
#         screen_width = monitor["width"]
#         screen_height = monitor["height"]
#         screen_size = (screen_width, screen_height)

#         codec = cv2.VideoWriter_fourcc(*"mp4v")
#         out = cv2.VideoWriter(filename, codec, fps, screen_size)

#         start_time = time.time()
#         while True:
#             img = np.array(sct.grab(monitor))
#             frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
#             out.write(frame)

#             if time.time() - start_time > duration:
#                 break

#         out.release()

#     st.success(f"Recording saved as {filename}.")

#     with open(filename, "rb") as video_file:
#         st.download_button(
#             label="📥 Download Recording",
#             data=video_file,
#             file_name=filename,
#         )
#     if st.button("🗑️ Delete Recording from Server"):
#         os.remove(filename)
#         st.success("Recording deleted from server.")


import streamlit as st  # type: ignore
import cv2  # type: ignore
import numpy as np  # type: ignore
import time
import os
from mss import mss  # type: ignore
import os

# Function to check if app is running on Streamlit Cloud
def is_streamlit_cloud():
    # Streamlit Cloud sets this environment variable
    return os.environ.get("STREAMLIT_ENVIRONMENT") == "cloud"

st.set_page_config(page_title="Screen recorder", layout="centered")
st.title("🎥 Screen Recorder - Python + Streamlit")

filename = st.text_input("Enter the filename", "recording.mp4")
duration = st.slider("Select the duration (seconds)", 10, 36000, 20)
fps = st.slider("Select the frame rate (FPS)", 1, 60, 30)

# Check if the app is running on Streamlit Cloud
if is_streamlit_cloud():
    st.warning("⚠️ Screen recording is disabled on Streamlit Cloud because screen access is not available.")
    st.info("Run this app locally to enable screen recording.")
else:
    if st.button("Start Recording"):
        st.success("Recording...")

        with mss() as sct:
            monitor = sct.monitors[1]  # Full screen
            screen_width = monitor["width"]
            screen_height = monitor["height"]
            screen_size = (screen_width, screen_height)

            codec = cv2.VideoWriter_fourcc(*"mp4v")
            out = cv2.VideoWriter(filename, codec, fps, screen_size)

            start_time = time.time()
            while True:
                img = np.array(sct.grab(monitor))
                frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
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

        if st.button("🗑️ Delete Recording from Server"):
            os.remove(filename)
            st.success("Recording deleted from server.")

