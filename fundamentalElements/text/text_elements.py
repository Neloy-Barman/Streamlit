import streamlit as st

# Title
st.title("This is a Title")

# Header
st.header("This is a Header")

# Subheader
st.subheader("This is a SubHeader")

# Markdown
st.markdown("This is a **Markdown** text.")
st.markdown("# Header1 using Markdown")
st.markdown("## Header1 using Markdown")

# Caption
st.caption("This is a Caption.")

# Code block
st.code("""
import pandas as pd
pd.read_csv("data.csv")
""")

# Preformatted text
st.text("This is a normal Text")

# LaTeX
st.latex("x=y^2")

# Divider
st.text("Text 1")
st.divider()
st.text("Text 2")

# Write
"""
    It is fairly a spceical function in streamlit because it can take a lot of arguments.
    We can display dataframe, integers or a bunch of things.
"""
st.write("This is a Write text.")
