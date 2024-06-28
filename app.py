import streamlit as st
from src.detect import detect_helmet, process_image
from PIL import Image
import io


st.title("Safety Helmet Detection")

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = process_image(uploaded_file)
    annotated_image, has_helmet = detect_helmet(image=image)
    st.image(
        annotated_image, caption="Processed Image", use_column_width=True
    )
    if has_helmet:
        st.success("Safety Helmet detected!")
    else:
        st.warning("No safety helmet detected!")

st.write("Upload an image to detect safety helmets.")

