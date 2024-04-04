import streamlit as st
import pandas as pd

df = pd.read_csv("data/sample.csv")

# Showing dataframe as dataframe
st.dataframe(data=df)

# Showing dataframe using write function
st.write(df)

# On both of the above functions we can interact with the dataframe, but using table, we can't do that.

st.table(df)

# Delta defines if we have change in the metrics.
st.metric(label="Population", value=900, delta=20, delta_color='normal')

# Negative change in value
st.metric(label="Expense", value=900, delta=-20, delta_color='normal')

# Inversing color than normal
st.metric(label="Expense", value=900, delta=-20, delta_color='inverse')

