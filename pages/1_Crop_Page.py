# pages/1_Crop_Page.py

import streamlit as st
from services.gemini_client import get_serpapi_context_and_run_agent

st.title("🌾 Ask KrishiMitra (AI Advisor)")
st.markdown("Ask anything about crops, organic farming, weather, pests, or government schemes.")

question = st.text_area("❓ Your Question", height=100)
pincode = st.text_input("📍 Your Pincode")
# use_web = st.checkbox("🔍 Search Internet Also", value=False) # We will use the pincode for context

if st.button("Get Answer"):
    with st.spinner("Fetching answer..."):
        answer = get_serpapi_context_and_run_agent(question=question, pincode=pincode)
        st.markdown(answer)