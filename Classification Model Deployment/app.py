import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
from sklearn.ensemble import GradientBoostingClassifier


# Function to load model
@st.cache_resource(show_spinner='Loading model......')
def load_model():
    pipe = load('model/pipe.joblib')
    return pipe


# Function to make a prediction
@st.cache_data(show_spinner="Making a prediction...")
def predict(_pipe, x_pred):
    features = [each[0] for each in x_pred]
    features = np.array(features).reshape(1, -1)
    pred = _pipe.predict(features)
    return pred[0]


if __name__ == "__main__":
    st.title("Mushroom classifier 🍄")
    
    st.subheader("Step 1: Select the values for prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        odor = st.selectbox('Odor', ('a - almond', 'l - anisel', 'c - creosote', 'y - fishy', 'f - foul', 'm - musty', 'n - none', 'p - pungent', 's - spicy'))
        stalk_surface_above_ring = st.selectbox('Stalk surface above ring', ('f - fibrous', 'y - scaly', 'k - silky', 's - smooth'))
        stalk_color_below_ring = st.selectbox('Stalk color below ring', ('n - brown', 'b - buff', 'c - cinnamon', 'g - gray', 'o - orange', 'p - pink', 'e - red', 'w - white', 'y - yellow'))
    with col2:
        gill_size = st.selectbox('Gill size', ('b - broad', 'n - narrow'))
        stalk_surface_below_ring = st.selectbox('Stalk surface below ring', ('f - fibrous', 'y - scaly', 'k - silky', 's - smooth'))
        ring_type = st.selectbox('Ring type', ('e - evanescente', 'f - flaring', 'l - large', 'n - none', 'p - pendant', 's - sheathing', 'z - zone'))
    with col3:
        gill_color = st.selectbox('Gill color', ('k - black', 'n - brown', 'b - buff', 'h - chocolate', 'g - gray', 'r - green', 'o - orange', 'p - pink', 'u - purple', 'e - red', 'w - white', 'y - yellow'))
        stalk_color_above_ring = st.selectbox('Stalk color above ring', ('n - brown', 'b - buff', 'c - cinnamon', 'g - gray', 'o - orange', 'p - pink', 'e - red', 'w - white', 'y - yellow'))
        spore_print_color = st.selectbox('Spore print color', ('k - black', 'n - brown', 'b - buff', 'h - chocolate', 'r - green', 'o - orange', 'u - purple', 'w - white', 'y - yellow'))

    st.subheader("Step 2: Ask the model for a prediction")

    pred_btn = st.button("Predict", type="primary")

    # If the button is clicked:

    if pred_btn:

        # Load the model
        pipe = load_model()

        x_pred = [odor, 
                    gill_size, 
                    gill_color, 
                    stalk_surface_above_ring, 
                    stalk_surface_below_ring, 
                    stalk_color_above_ring, 
                    stalk_color_below_ring, 
                    ring_type, 
                    spore_print_color]
        

        # 5. Make a prediction
        pred = predict(pipe, x_pred)
        print(pred)

        # 6. Format the prediction to be a nice text
        nice_pred = "The mushroom is poisonus 🤢" if pred == "p" else "The mushroom is edible 🍴"
        
        # 7. Output it to the screen
        st.write(nice_pred)
    