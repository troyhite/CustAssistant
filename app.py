import streamlit as st
from codeautogen import codeautogen
from digiassist import digiassit
from semroute import semroute

# Set page size
st.set_page_config(
    page_title="Gen AI Application Validation",
    page_icon=":rocket:",
    layout="wide",  # or "centered"
    initial_sidebar_state="expanded"  # or "collapsed"
)

# Load your CSS file
def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Call the function to load the CSS
load_css("styles.css")

st.logo("bblogo1.png")
st.sidebar.image("bblogo1.png", use_column_width=True)

# Sidebar navigation
nav_option = st.sidebar.selectbox("Navigation", ["Home", "Code Autogen", 
                                                 "Shopping Cart",
                                                  "semroute", "About"])

# Display the selected page
if nav_option == "Code Autogen":
    codeautogen()
elif nav_option == "Shopping Cart":
    digiassit()
elif nav_option == "semroute":
    semroute()
#elif nav_option == "VisionAgent":
#    vaprocess()

st.sidebar.image("microsoft-logo-png-transparent-20.png", use_column_width=True)