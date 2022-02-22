import streamlit as st

def initialize_view():
    country = st.sidebar.text_input('Input country')
    st.write(country)