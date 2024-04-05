import datetime
import streamlit as st

form = st.form(key="order_form", clear_on_submit=True)

with form:
    st.write("What would you like to order")
    
    appetizers = st.selectbox(label="Appetizers", options=["choice1", "choice2", "choice3"], index=0)
    
    mainCourse = st.selectbox(label="Main Course", options=["choice1", "choice2", "choice3"], index=0)

    dessert = st.selectbox(label="Dessert", options=["choice1", "choice2", "choice3"], index=0)

    checkBox = st.checkbox("Are you bringing your own wine?")

    today = datetime.date.today()
    date = st.date_input(label="When are you coming?", value="today", max_value=datetime.date(2024, 12, 31), min_value=today)

    time = st.time_input(label="At what time are you coming?", value="now", step=1800)

    allergies = st.text_area("Any allergies?", placeholder="Leave us a note for allergies", max_chars=100, height=200)

    submitted = st.form_submit_button("Submit", type="secondary")

if submitted:
    st.write("Your order summary: ")
    st.write(f"Appetizer: {appetizers}")
    st.write(f"Main course: {mainCourse}")
    st.write(f"Dessert: {dessert}")
    st.write(f"Are you bringing your own wine: {"Yes" if checkBox else "No"}")
    st.write(f"Date of visit: {date}")
    st.write(f"Time of visit: {time}")
    st.write(f"Allergies: {allergies}")
