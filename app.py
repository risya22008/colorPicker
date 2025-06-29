import streamlit as st
import numpy as np
import cv2
from sklearn.cluster import KMeans
from collections import Counter
from matplotlib import colors

def get_dominant_colors(image, k=8):
    # Convert image from BGR to RGB and reshape it
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    
    # Apply KMeans to find dominant colors
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(image)
    
    # Count color frequencies and get cluster centers
    counts = Counter(kmeans.labels_)
    centers = kmeans.cluster_centers_
    
    # Order colors by frequency and convert to HEX
    ordered_colors = [centers[i] for i in counts.keys()]
    hex_colors = [colors.rgb2hex(ordered_colors[i] / 255.0).upper() for i in range(k)]
    rgb_colors = [ordered_colors[i] for i in range(k)]
    
    return hex_colors, rgb_colors

def display_color_palette(hex_colors, rgb_colors):
    # Display the color palette
    st.markdown('<div style="display: flex; flex-wrap: wrap; justify-content: center;">', unsafe_allow_html=True)
    for hex_color, rgb_color in zip(hex_colors, rgb_colors):
        rgb_text = f"RGB({int(rgb_color[0])}, {int(rgb_color[1])}, {int(rgb_color[2])})"
        st.markdown(f'''
        <div style="text-align: center; margin: 20px; width: 200px; font-family: Arial, sans-serif;">
            <div style="display: inline-block; width: 140px; height: 140px; background-color: {hex_color}; border-radius: 20px; border: 2px solid #000; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); overflow: hidden;">
            </div>
            <div style="margin-top: 15px; font-weight: bold; color: #333; font-size: 18px;">Color Palette</div>
            <div style="font-size: 14px; color: #666; margin-top: 10px;">Hex: {hex_color}</div>
            <div style="font-size: 14px; color: #666;">RGB: {rgb_text}</div>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Streamlit UI
st.set_page_config(page_title="Color Picker Generator", page_icon=":art:", layout="wide")

st.title("🎨 Color Picker Generator 🎨")
st.markdown("""
    Upload an image and discover the 8 most dominant colors in it as a color palette.
    """)

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "heic"])

if uploaded_file is not None:
    # Read and decode the uploaded image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Display the uploaded image
    st.image(image_rgb, caption='Uploaded Image', use_column_width=True, channels='RGB')
    
    st.write("Generating palette...")
    try:
        hex_colors, rgb_colors = get_dominant_colors(image)
        st.write("Here are the 8 most dominant colors in the image:")
        display_color_palette(hex_colors, rgb_colors)
    except Exception as e:
        st.error(f"Error processing the image: {str(e)}. Please make sure it's a valid image file.")
else:
    st.info("Please upload an image to generate the color palette.")
