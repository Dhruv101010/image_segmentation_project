import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from PIL import Image
import os
from captioning.caption_model import generate_caption
from segmentation.mask_rcnn import segment_image

st.title("🖼️ Image Captioning + 🎯 Segmentation App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image_path = f"temp_{uploaded_file.name}"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.read())

    st.image(image_path, caption="Uploaded Image", use_column_width=True)

    st.subheader("📃 Caption:")
    caption = generate_caption(image_path)
    st.write(f"**{caption}**")

    st.subheader("🧩 Segmented Image:")
    segmented = segment_image(image_path)
    st.image(segmented, caption="Objects Detected", use_column_width=True)

    os.remove(image_path)