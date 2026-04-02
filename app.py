import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page config
st.set_page_config(page_title="Spam Detector", page_icon="📧", layout="centered")

# Custom UI
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f7;
    }
    .title {
        text-align: center;
        font-size: 40px;
        color: #2c3e50;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📧 AI Spam Email Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter your email content below</div>', unsafe_allow_html=True)

# Input
email = st.text_area("✉️ Email Content", height=150)

# Button
if st.button("🔍 Check Email"):
    if email.strip() != "":
        data = vectorizer.transform([email.lower()])
        result = model.predict(data)

        if result[0] == 1:
            st.error("🚫 This is SPAM Email")
        else:
            st.success("✅ This is NOT SPAM Email")
    else:
        st.warning("⚠️ Please enter email text")

# Footer
st.markdown("---")
st.markdown("💡 Developed using Streamlit | AI Project")