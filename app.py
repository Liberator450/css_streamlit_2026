import streamlit as st
import time

# Page config
st.set_page_config(
    page_title="Urgent Message",
    page_icon="✨",
    layout="centered"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
@keyframes fadeInUp {
    0% {
        opacity: 0;
        transform: translateY(40px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.main-title {
    font-size: 3rem;
    font-weight: 800;
    text-align: center;
    color: #ffffff;
    animation: fadeInUp 1.2s ease-out;
}

.subtitle {
    font-size: 1.2rem;
    text-align: center;
    color: #d1d5db;
    margin-top: 10px;
    animation: fadeInUp 1.5s ease-out;
}

.message-box {
    background: linear-gradient(135deg, #7c3aed, #ec4899);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    color: white;
    font-size: 2rem;
    font-weight: 700;
    margin-top: 30px;
    animation: fadeInUp 1s ease-out, pulse 2s infinite;
    box-shadow: 0px 20px 40px rgba(0,0,0,0.25);
}

.stButton > button {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    font-size: 1.1rem;
    padding: 12px 30px;
    border-radius: 30px;
    border: none;
    animation: pulse 2s infinite;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #16a34a, #15803d);
}
</style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("<div class='main-title'>🚨 Urgent Message 🚨</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Click the button below to see an urgent message from <b>Mkhululi</b></div>",
    unsafe_allow_html=True
)

st.write("")  
st.write("")

# Button interaction
if "show_message" not in st.session_state:
    st.session_state.show_message = False

if st.button("👀 Show Message"):
    with st.spinner("Opening message..."):
        time.sleep(1.5)
    st.session_state.show_message = True

# Animated Message Reveal
if st.session_state.show_message:
    st.markdown("""
    <div class="message-box">
        Jola manje umdala mumngaka 😄🔥
    </div>
    """, unsafe_allow_html=True)
