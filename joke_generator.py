import streamlit as st
import requests

def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    joke = response.json()
    return f"{joke['setup']} - {joke['punchline']}"
st.title("Random Joke Generator 😄")
st.write("Click the button to get a random joke! 🤔")

if st.button('Get Joke 🤣'):
    joke = fetch_joke()
   
    st.markdown(f"""
    <style>
    .joke-text {{
        font-size: 24px;
        color: #2980b9;
        text-align: center;
        font-weight: bold;
        margin-top: 20px;
        background-color: #ecf0f1;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }}
    </style>
    """, unsafe_allow_html=True)
    st.markdown(f'<div class="joke-text">{joke} 😆</div>', unsafe_allow_html=True)
