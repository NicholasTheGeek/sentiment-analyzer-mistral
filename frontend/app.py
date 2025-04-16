import streamlit as st
import requests

#App Configuration
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

#Custom Styling
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        h1 {
            color: #0a58ca;
        }
        .stTextArea textarea {
            font-size: 16px;
        }
        .stButton>button {
            background-color: #0a58ca !important;
            color: white !important;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 1em;
            border: none;
            box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        }
        .stButton>button:hover {
            background-color: #084298 !important;
            transform: scale(1.02);
        }
    </style>
 """, unsafe_allow_html=True)

#UI Title and Subtitle
st.title("Sentiment Analyzer (Mistral)")
st.caption("Built with FastAPI + Ollama + Streamlit")

#Text Input
text_input = st.text_area("Enter your sentence below:", height=150)

#Analyze Button
if st.button("Analyze"):
    if not text_input.strip():
        st.warning("Please enter text to analyze.")
    else:
        with st.spinner("Analyzing sentiment using Mistral..."):
            try:
                res = requests.post("http://localhost:8000/analyze/", data={"text": text_input})
                sentiment = res.json().get("sentiment", "Error")
                st.success("Prediction Complete!")
                st.subheader("Predicted Sentiment:")
                st.markdown(f"<div style='color:#000000; text-align:center; font-weight:600;'>{sentiment}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error("Could not connect to the FastAPI backend. Please make sure its running.")        
