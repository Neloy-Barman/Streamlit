import streamlit as st
import pandas as pd

# Buttons

# Primary
primary = st.button(label="Primary", type="primary")
if primary:
    st.write("Hello from primary!!")

# Secondary
secondary = st.button(label="Secondary", type="secondary")
if secondary:
    st.write("Hello from secondary!!")

st.divider()

# Checkbox
checkbox = st.checkbox("Remember Me")
if checkbox:
    st.write("You will be remembered!!")

st.divider()

# Radio buttons
# radio = st.radio("Choose one", options=["Male", "Female"], index=0, horizontal=False)
radio = st.radio("Choose one", options=["Male", "Female"], index=0, horizontal=True)
st.write(radio)

st.divider()

# Selectbox
select = st.selectbox("Choose one", options=["Student", "Professional", "Employee"], index=0)
st.write(select)

st.divider()

# Multiselect
multiSelect = st.multiselect(label="Choose as many as you want.", default="Data Science", options=["Data Science", "Machine learning", "Data Analytics"], max_selections=2)
st.write(multiSelect)

st.divider()

# Slider
slider = st.slider("Pick a number", max_value=10, min_value=0, step=1, value=3)
st.write(slider)

st.divider()

# Text Input
text = st.text_input(label="What's your name", placeholder="John Doe")
st.write(f"Your name is: {text}")

st.divider()

# Number Input
number = st.number_input(label="Pick a number", max_value=10, min_value=0, step=1, value=2)
st.write(f"You have choosen: {number}")

st.divider()

# Text Area
text_arr = st.text_area(label="What do you want to tell me?", height=200, placeholder="Write your message here", max_chars=200)
st.write(text_arr)

st.divider()


