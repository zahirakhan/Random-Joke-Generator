import streamlit as st
import requests

def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    joke = response.json()
    return f"{joke['setup']} - {joke['punchline']}"

st.markdown("""
    <style>
    .title {
        font-size: 40px;
        color: #f39c12;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
    }
    .button {
        background-color: #27ae60;
        color: white;
        font-size: 20px;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease;
    }
    .button:hover {
        background-color: #2ecc71;
    }
    .joke {
        font-size: 24px;
        color: #2980b9;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Random Joke Generator 😄</div>', unsafe_allow_html=True)
st.write("Click the button to get a random joke! 🤔")

if st.button('Get Joke 🤣', key="joke_button"):
    joke = fetch_joke()
    st.markdown(f'<div class="joke">{joke} 😆</div>', unsafe_allow_html=True)
