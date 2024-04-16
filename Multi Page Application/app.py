import streamlit as st
import pandas as pd

# Set page configuration
# Page config must be the first element in the script.

# page_title: The title that appears in the browser
# page_icon: The icon that appears in the browser with title
# layout: Whether the elements will be at center or in wider range 
# initial_sidebar_state: Whether the sidebar to be showed or not initially 

st.set_page_config(
    page_title="Homepage",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="auto"
)


# Just to see the access of data between different pages

# # Initialize a sample df and store it in the session state
# df = pd.DataFrame({
#     "col1": [1, 2, 3],
#     "col2": [4, 5, 6]
# }) 

# if "df" not in st.session_state:
#     st.session_state["df"] = df


# # Initialize state with the key "product" set to 0
# if "product" not in st.session_state:
#     st.session_state["product"] = 0

# Initialize all the kwys with values that I want to keep
if all(key not in st.session_state.keys() for key in ("product", "x1", "x2")):
    st.session_state["x1"] = 0
    st.session_state["x2"] = 0
    st.session_state["product"] = 0

# Function to keep a value (Copy from temporary key to permanent key)
def keep(key):
    st.session_state[key] = st.session_state[f"_{key}"]

# Function to reassign value to temporary key (Copy from permanent key to temporary key)
def unkeep(key):
    st.session_state[f"_{key}"] = st.session_state[key]

# Define a function to multiply two numbers
def multiply(x1, x2):
    st.session_state["product"] = x1*x2

if __name__ == "__main__":
    st.title("Homepage")

    col1, col2 = st.columns(2)

    with col1:
        unkeep("x1")
        x1 = st.number_input("Pick a number", 0, 10, key="_x1", on_change=keep, args=("x1",))
    with col2:
        unkeep("x2")
        x2 = st.number_input("Pick another number", 0, 10, key="_x2", on_change=keep, args=("x2",))

    st.button("Multiply!", type="primary", on_click=multiply, args=(x1, x2))
    # st.button("Multiply!", type="primary", on_click=multiply, kwargs=dict(x1 = x1, x2 = x2))


st.write(st.session_state)