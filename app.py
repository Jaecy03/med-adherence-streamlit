import streamlit as st
import pandas as pd

st.title("Medication Adherence Support")

name = st.text_input("Enter your name")
med_time = st.time_input("Set your medication time")

if st.button("Confirm Reminder"):
    st.success(f"Hi {name}, we'll remind you at {med_time}!")

st.write("This is a basic Streamlit app to demonstrate medication reminder setup.")
