import streamlit as st
import pandas as pd

st.title("Stats App")


df = pd.read_csv('/Users/daivik/Desktop/streamlit app/mcbb_stats.csv')


player_selection = st.selectbox(
    "Select a player",
    df['Name'].unique()
)

df['2FG %'] = df['2FG %'].str.strip('%')
df['3FG %'] = df['3FG %'].str.strip('%')
df['TFG %'] = df['TFG %'].str.strip('%')
df['FT %'] = df['FT %'].str.strip('%')
df.drop(range(17, df.shape[0] , 18))

def average_stat(player_name, stat):
    player_data = df[df['Name'].str.lower() == player_name.lower()]
    valid_data = player_data[pd.to_numeric(player_data[stat], errors='coerce').notna()]
    return valid_data[stat].astype(float).mean()

# Display average statistics
if st.button("Calculate Averages"):
    st.write(f"Averages for {player_selection.title()}:")
    st.write(f"PPG: {average_stat(player_selection, 'PTS'):.1f}")
    st.write(f"RPG: {average_stat(player_selection, 'TOTAL REB'):.1f}")
    st.write(f"APG: {average_stat(player_selection, 'AST'):.1f}")
    st.write(f"BPG: {average_stat(player_selection, 'BLK'):.1f}")
    st.write(f"SPG: {average_stat(player_selection, 'STL'):.1f}")
    st.write(f"TOV: {average_stat(player_selection, 'TOV'):.1f}")
