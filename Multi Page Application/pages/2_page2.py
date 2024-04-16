import streamlit as st

product = st.session_state["product"]

st.subheader(f"The product is {product}")

st.write(st.session_state)