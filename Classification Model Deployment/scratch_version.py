import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.ensemble import GradientBoostingClassifier


COLS = ['class', 'odor', 'gill-size', 'gill-color', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'ring-type', 'spore-print-color']


# Function to read the data
@st.cache_data(show_spinner="Fetching data ")
def read_csv(cols):
    df = pd.read_csv('data/mushrooms.csv')
    df = df[cols]
    return df


# Function to fit the LabelEncoder
@st.cache_resource
def encode_label(df: pd.DataFrame, column: str) -> pd.DataFrame:
    le = LabelEncoder()
    le.fit_transform(df[column])
    return le


# Function to fit the OrdinalEncoder
@st.cache_resource
def ordinal_encode(df: pd.DataFrame) -> pd.DataFrame:
    oe = OrdinalEncoder()
    x_cols = df.columns[1:]
    oe.fit_transform(df[x_cols])
    return oe


# Function to encode data
@st.cache_data(show_spinner="Encoding data......")
def encode_data(df: pd.DataFrame, column: str, _x_encoder, _y_encoder):
    df[column] = _y_encoder.transform(df[column])
    x_cols = df.columns[1:]
    df[x_cols] = _x_encoder.transform(df[x_cols])
    return df


# Function to train the model
@st.cache_resource(show_spinner="Training model....")
def train(df, column):
    x = df.drop([column], axis=1)
    y = df[column]

    gbc = GradientBoostingClassifier(max_depth=5, random_state=42)
    gbc.fit(X=x, y=y)
    return gbc


# Function to make a prediction
@st.cache_data(show_spinner="Making a prediction...")
def predict(_model, _x_encoder, x_pred):
    features = [each[0] for each in x_pred]
    features = np.array(features).reshape(1, -1)
    encoded_features = _x_encoder.transform(features)
    pred = _model.predict(encoded_features)
    return pred[0]


if __name__ == "__main__":
    st.title("Mushroom classifier 🍄")
    
    # Read the data
    df = read_csv(cols=COLS)
    
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
    # 1. Fit the LabelEncoder
    # 2. Fit the OrdinalEncoder
    # 3. Encode the data
    # 4. Train the model

    if pred_btn:
        # Fitting the LabelEncoder
        le = encode_label(df=df, column='class')

        # Fitting the OridinalEncoder
        oe = ordinal_encode(df=df)

        # Encoding data
        encoded_df = encode_data(df, 'class', oe, le)

        # Train the model
        model = train(df=encoded_df, column='class')

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
        pred = predict(model, oe, x_pred)
        print(pred)

        # 6. Format the prediction to be a nice text
        nice_pred = "The mushroom is poisonus 🤢" if pred else "The mushroom is edible 🍴"
        
        # 7. Output it to the screen
        st.write(nice_pred)
    



