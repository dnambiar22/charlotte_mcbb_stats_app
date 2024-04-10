import streamlit as st

st.title("Stats App")

player_selection = st.selectbox(
    "Select a player",
    ("Option 1", "Option 2", "Option 3")
)
