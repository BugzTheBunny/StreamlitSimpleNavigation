import streamlit as st
from views import demo_view_1,demo_view_2

NAVIGATION_ITEMS = {
    'Name App': demo_view_1,
    'Country App': demo_view_2,
}

def inject_css_file(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>',
                    unsafe_allow_html=True)

def nav_component():
    navigation = st.sidebar.selectbox('Go to',[view for view in NAVIGATION_ITEMS])
    return NAVIGATION_ITEMS[navigation]
    