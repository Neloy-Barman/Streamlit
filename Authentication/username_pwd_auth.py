import streamlit as st

# Initialize state to:
# Store the username
# Store the password
# Check if the password is correct
# Check if the form is submitted

# Initializing session state
if all(key not in st.session_state.keys() for key in ("username", "pwd", "pwd_correct", "form_submitted")):
    st.session_state["pwd"] = ""
    st.session_state["username"] = ""
    st.session_state["pwd_correct"] = False
    st.session_state["form_submitted"] = False

# Function to check if the password is correct
def check_login():
    st.session_state["form_submitted"] = True

    if st.session_state["username"] in st.secrets["passwords"] and st.session_state["pwd"] == st.secrets["passwords"][st.session_state["username"]]:
        st.session_state["pwd"] = ""
        st.session_state["username"] = ""
        st.session_state["pwd_correct"] = True
    else:
        st.session_state["pwd_correct"] = False

# Function to display the login form
def display_login_form():
    with st.form("Login"):
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", key="pwd")
        
        st.form_submit_button("Login", on_click=check_login)

if not st.session_state['pwd_correct'] and not st.session_state["form_submitted"]:
    display_login_form()
elif not st.session_state['pwd_correct'] and st.session_state['form_submitted']:
    display_login_form()
    st.error("Invalid username/password")
elif st.session_state["pwd_correct"] and st.session_state["form_submitted"]:
    st.write("User logged in")
else:
    display_login_form()

st.write(st.session_state)