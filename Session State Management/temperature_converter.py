import streamlit as st
st.title("Exercise: State Management")
st.header("Temperature conversion")

if "celsius" not in st.session_state:
    st.session_state['celsius'] = 0.00

if "farenheit" not in st.session_state:
    st.session_state['farenheit'] = 32.00

if "kelvin" not in st.session_state:
    st.session_state['kelvin'] = 273.15

col1, col2, col3 = st.columns(3)

def celsiusval():
    value = st.session_state['celsius']
    st.session_state['farenheit'] = value * (9/5) + 32.00
    st.session_state['kelvin'] = value + 273.15

def farenheitval():
    value = st.session_state['farenheit']
    st.session_state['celsius'] = (value - 32.00) * (5/9)
    st.session_state['kelvin'] = st.session_state['celsius'] + 273.15

def kelvinval():
    value = st.session_state['kelvin']
    st.session_state['celsius'] = value - 273.15
    st.session_state['farenheit'] = st.session_state['celsius'] * (9/5) + 32.00

def addVal(value):
    st.session_state['celsius'] += value
    celsiusval()

with col1:
    st.number_input("Celsius", step=0.01 , key="celsius", on_change=celsiusval)
    value = st.number_input("Add to Celsius", step=1)
    st.button(type="primary", label="Add", on_click=addVal, args=(value, ))

with col2:
    st.number_input("Farenheit", step=0.01, key="farenheit", on_change=farenheitval)

with col3:
    st.number_input("Kelvin", step=0.01, key="kelvin", on_change=kelvinval)

col4, col5, col6 = st.columns(3)

def setTemperatures(celsius, farenheit, kelvin):
    st.session_state["celsius"] = celsius
    st.session_state["farenheit"] = farenheit
    st.session_state["kelvin"] = kelvin


with col4:
    st.button(type="secondary", label="🧊 Freezing point of water", on_click=setTemperatures, kwargs=dict(celsius = 0.00, farenheit = 32.00, kelvin = 273.15))
    
with col5:
    st.button(type="secondary", label="🔥Boiling point of water", on_click=setTemperatures, kwargs=dict(celsius = 100.00, farenheit = 212.00, kelvin = 373.15))

with col6:
    st.button(type="secondary", label="🥶 Absolute zero", on_click=setTemperatures, kwargs=dict(celsius = -273.15, farenheit = -459.67, kelvin = 0.00))

st.write(st.session_state)

