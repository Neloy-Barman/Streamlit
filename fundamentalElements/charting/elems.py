import streamlit as st
import pandas as pd
import matplotlib.pyplot  as plt

df = pd.read_csv("data/sample.csv")

# Line plot
st.line_chart(data=df, x="year", y=["col1", "col2", "col3"])

# Area chart
st.area_chart(data=df, x="year", y=["col1", "col2", "col3"])

# Bar chart
st.bar_chart(data=df, x="year", y=["col1", "col2", "col3"])

# If we have latitude and longitude values, we can show a map
map = pd.read_csv("data/map.csv")
st.map(map)

# In the above ones, those are the default by streamlit, we can't change anything there.

# Matplotlib plot
fig, ax = plt.subplots()
ax.plot(df.year, df.col1)
ax.set_title("My Figure Title")
ax.set_xlabel("X label")
ax.set_ylabel("Y label")
fig.autofmt_xdate()

st.pyplot(fig=fig)