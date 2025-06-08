# app.py

import streamlit as st
import os
import sys

# Add the project root to the Python path
# This allows importing modules from 'services' and 'config' directories
# even when running from the root directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir)
sys.path.insert(0, project_root)

# Import the necessary environment variables from config.py
# This ensures that API keys are loaded before any services that use them.
from config.config import GOOGLE_API_KEY, SERPAPI_API_KEY

# Set environment variables for LangChain and other services
# os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
# os.environ["SERPAPI_API_KEY"] = SERPAPI_API_KEY

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="KrishiMitra - AI Agricultural Advisor",
    page_icon="🌾",
    layout="wide", # Can be "wide" or "centered"
    initial_sidebar_state="auto", # Can be "auto", "expanded", or "collapsed"
)

# Main title for the application
st.title("Welcome to KrishiMitra 🌾")
st.markdown("Your AI-powered agricultural advisor for Indian farmers.")

st.sidebar.title("Navigation")
st.sidebar.markdown("Use the links below to navigate through the app.")

# You can add more content to the main app.py if needed,
# or simply direct users to the pages in the sidebar.

# Streamlit automatically discovers pages in the 'pages/' directory
# if they are named with a number prefix (e.g., '1_Crop_Page.py').
# The sidebar will automatically populate with these pages.

# You can add some introductory text or a call to action on the main page
st.write(
    """
    KrishiMitra is designed to assist Indian farmers with various aspects of agriculture,
    from crop advice to pest management and government schemes.
    """
)

st.info("👈 Select a page from the sidebar to get started!")

# The content of '1_Crop_Page.py' will be accessible via the sidebar
# once the Streamlit app is run.
