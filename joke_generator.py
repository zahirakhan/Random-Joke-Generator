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
    st.write(f"Here's your joke: {joke} 😆")
