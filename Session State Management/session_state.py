import streamlit as st

st.title("Stateful apps")

st.write("Here is the session state: ")
st.write_stream(st.session_state)
st.button("Update state", type='secondary')

# Set the value using the key-value syntax
if "key" not in st.session_state:
    st.session_state["key"] = "value"

# Set the value using the attribute syntax
if "attribute" not in st.session_state:
    st.session_state.attribute = "another value"

# Read value from session state
st.write(f"Reading with key-value syntax: {st.session_state['key']}")

st.write(f"Reading with the attribute syntax: {st.session_state.attribute}")

# Update values in state
st.session_state["key"] = "new value"
st.session_state.attribute = "updated value"

# Delete item in state
del st.session_state["key"]
del st.session_state.attribute

