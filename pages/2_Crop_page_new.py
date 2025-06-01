# pages/1_Crop_Page.py

import streamlit as st
from services.gemini_client import get_serpapi_context_and_run_agent
import streamlit.components.v1 as components # Import components for HTML/JS injection

st.title("🌾 Ask KrishiMitra (AI Advisor)")
st.markdown("Ask anything about crops, organic farming, weather, pests, or government schemes.")

# Input fields for question and pincode
question = st.text_area("❓ Your Question", height=100, key="question_input")
pincode = st.text_input("📍 Your Pincode", key="pincode_input")

# Initialize session state for answer text if it doesn't exist
# This ensures the answer persists across Streamlit reruns
if 'answer_text' not in st.session_state:
    st.session_state.answer_text = ""

# Button to trigger the answer generation
if st.button("Get Answer", key="get_answer_button"):
    if question and pincode:
        with st.spinner("Fetching answer..."):
            # Call the function to get the answer from the AI advisor
            answer = get_serpapi_context_and_run_agent(question=question, pincode=pincode)
            # Store the answer in session state
            st.session_state.answer_text = answer
    else:
        st.warning("Please enter both a question and a pincode to get advice.")

# Dedicated text box to display the answer
# This box will only appear once an answer has been generated
if st.session_state.answer_text:
    st.subheader("Your Answer:")
    st.text_area(
        label="Answer from KrishiMitra:",
        value=st.session_state.answer_text,
        height=300,
        disabled=True, # Make the text area read-only
        key="display_answer_box", # Unique key for the text area
        help="This is the detailed advice from KrishiMitra."
    )

    # Button to copy the answer to the clipboard
    # Using a clipboard emoji for the icon
    if st.button("📋 Copy Answer", key="copy_button"):
        # JavaScript to perform the copy operation
        # We use a temporary textarea element to leverage document.execCommand('copy')
        # The text to copy is taken from st.session_state.answer_text
        # Backticks are used for template literals in JS, and any existing backticks
        # in the answer text are escaped to prevent syntax errors.
        js_code = f"""
        <script>
            var textToCopy = `{st.session_state.answer_text}`;
            var tempInput = document.createElement('textarea');
            tempInput.value = textToCopy;
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand('copy');
            document.body.removeChild(tempInput);
        </script>
        """
        # Inject the JavaScript into the Streamlit app.
        # Setting height and width to 0 makes the component invisible.
        components.html(js_code, height=0, width=0)

        # Display a success message in Streamlit to confirm the copy operation
        st.success("Answer copied to clipboard!")

