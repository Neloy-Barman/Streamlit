import streamlit as st


# Initializing the session state
# Dictionary-like syntax
if key not in st.session_state:
    st.session_state['key'] = ValueError

# Attribute Syntax
if key not in st.session_state:
    st.session_state.key = value


# Read operation
# Dictionary-like syntax
st.write(st.session_state['key'])

# Attribute syntax
st.write(st.session_state.key)


# Delete operation
# Dictionary-like syntax
del st.session_state['key']

# Attribute syntax
for key in st.session_state.keys():
    del st.session_state[key]


# Update operation
# Dictionary-like syntax
st.session_state['key'] = new_value

# Attribute syntax
st.session_state.key = new_value




