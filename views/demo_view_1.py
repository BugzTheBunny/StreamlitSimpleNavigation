import streamlit as st

def initialize_view():
    name = st.sidebar.text_input('Input name')
    st.write(name)