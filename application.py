import streamlit as st
import utilities as utils
# Application initialization and configuration
# ---------------
# Settings
st.set_page_config(layout="wide", page_title='Inshop Analytics tool')
st.set_option('deprecation.showPyplotGlobalUse', False)
# ---------------
# Loading CSS
utils.inject_css_file("static/styles.css")
# ---------------

def main():
    view = utils.nav_component()
    view.initialize_view()

if __name__ == '__main__':
    main()
    