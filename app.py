import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_image_coordinates import streamlit_image_coordinates

# Load color dataset
@st.cache_data
def load_colors():
    df = pd.read_csv("colors.csv")
    return df

color_data = load_colors()
st.write("🎨 Loaded Color Data Sample:")
st.dataframe(color_data.head())

# Find closest color name
def get_color_name(R, G, B, color_data):
    min_dist = float('inf')
    closest_color = {'color_name': 'Unknown', 'hex': '#000000'}

    for _, row in color_data.iterrows():
        try:
            d = ((R - int(row['R'])) ** 2 +
                 (G - int(row['G'])) ** 2 +
                 (B - int(row['B'])) ** 2)
            if d < min_dist:
                min_dist = d
                closest_color = {
                    'color_name': row['color_name'],
                    'hex': row['hex']
                }
        except Exception as e:
            st.write(f"Error reading row: {row} - {e}")

    return closest_color

# Streamlit UI
st.title("🎨 Color Detection from Image (No OpenCV)")
