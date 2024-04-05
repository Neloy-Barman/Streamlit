import pandas as pd
import streamlit as st

# Sidebar
sidebar = st.sidebar
with st.sidebar:
    st.write("Text in the sidebar")

# Columns
col1, col2, col3 = st.columns(3)

col1.write("This is a column")

slider = col2.slider("Choose a number", min_value=0, max_value=10, step=2)

col3.write(slider)

st.divider()

# Tabs
df = pd.read_csv("data/sample.csv")

tab1, tab2 = st.tabs(["Line chart", "Bar plot"])

with tab1:
    tab1.write("A Line Plot")
    st.line_chart(df, x="year", y=["col1", "col2", "col3"])

with tab2:
    tab2.write("A Bar Plot")
    st.bar_chart(data=df, x="year", y=["col1","col2", "col3"])

st.divider()

# Expander (Collapsable element)
with st.expander("Click to expand"):
    st.write("I am text that you only see when you expand")

st.divider()

# Container
with st.container(border=True):
    st.write("This is inside the container")

st.write("This is outside the container")


