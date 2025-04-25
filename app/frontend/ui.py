import streamlit as st
import requests

from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

# Initialize logger
logger = get_logger(__name__)

# Streamlit UI setup
st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("Groq-based AI Chatbot Agent")

# Inputs
system_prompt = st.text_area("Define your AI Agent: ", height=70)
selected_model = st.selectbox("Select Groq Model:", settings.ALLOWED_MODEL_NAMES)
allow_web_search = st.checkbox("Allow Web Search")
user_query = st.text_area("Enter your query: ", height=150)

API_URL = "http://127.0.0.1:9999/chat"

# Button logic
if st.button("Ask Agent!") and user_query.strip():
    payload = {
        "model_name": selected_model,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allow_web_search
    }

    try:
        logger.info(f"Sending request to backend with model: {selected_model}")
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            agent_response = response.json().get("response", "")
            logger.info("Successfully received response from backend")
            st.subheader("Agent Response")
            st.markdown(agent_response.replace("\n", "<br>"), unsafe_allow_html=True)
        else:
            logger.error(f"Backend returned error: {response.status_code} - {response.text}")
            st.error(f"Error {response.status_code}: {response.text}")

    except Exception as e:
        logger.exception("Exception occurred while sending request to backend")
        st.error(str(CustomException("Failed to communicate with AI backend", error_detail=e)))
