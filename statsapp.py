import streamlit as st
import pandas as pd

st.title("Charlotte Men's Club Basketball 2023-24 Stats App")

# Reading in the data from local desktop 
df = pd.read_csv('/Users/daivik/Desktop/streamlit app/mcbb_stats.csv')

# Selecting a player
player_selection = st.selectbox(
    "Select a player",
    [''] + df['Name'].unique()
)

# Cleaning data that was not needed from csv 
df['2FG %'] = df['2FG %'].str.strip('%')
df['3FG %'] = df['3FG %'].str.strip('%')
df['TFG %'] = df['TFG %'].str.strip('%')
df['FT %'] = df['FT %'].str.strip('%')
df.drop(range(17, df.shape[0], 18))


# Spacing out columns for better viewing
col1, col2, col3 = st.columns(3)

# function (1), displays players average stats for all basic categories 
def average_stat(player_name, stat):
    player_data = df[df['Name'].str.lower() == player_name.lower()]
    valid_data = player_data[pd.to_numeric(player_data[stat], errors='coerce').notna()]
    return valid_data[stat].astype(float).mean()

        
# function (2), displays players average shooting percentages 
def shooting_splits(player_name, stat, stat2, stat3):
    average_value1 = average_stat(player_name, stat)
    average_value2 = average_stat(player_name, stat2)
    average_value3 = average_stat(player_name, stat3)
        
# function (3), displays misc. stats 
def misc_stats(player_name, stat, stat2, stat3):
    average_value = average_stat(player_name, stat)
    average_value2 = average_stat(player_name, stat2)
    average_value3 = average_stat(player_name, stat3)

# Displaying all stats 
if st.button("Calculate All Stats"):
    col1.write(f"Averages for {player_selection.title()}:")
    col1.write(f"PPG: {average_stat(player_selection, 'PTS'):.1f}")
    col1.write(f"RPG: {average_stat(player_selection, 'TOTAL REB'):.1f}")
    col1.write(f"APG: {average_stat(player_selection, 'AST'):.1f}")
    col1.write(f"BPG: {average_stat(player_selection, 'BLK'):.1f}")
    col1.write(f"SPG: {average_stat(player_selection, 'STL'):.1f}")
    col1.write(f"TOV: {average_stat(player_selection, 'TOV'):.1f}")
    col2.write(f"Shooting Splits for {player_selection.title()}:")
    col2.write(f"2FG: {average_stat(player_selection, '2FG %'):.1f}%")
    col2.write(f"3FG: {average_stat(player_selection, '3FG %'):.1f}%")
    col2.write(f"TFG: {average_stat(player_selection, 'TFG %'):.1f}%")
    col2.write(f"FT: {average_stat(player_selection, 'FT %'):.1f}%")
    col3.write(f"Miscellaneous stats for {player_selection.title()}:")
    col3.write(f"Average Game Score: {average_stat(player_selection, 'G-SCORE'):.1f}")
    col3.write(f"Hustle Plays (per game): {average_stat(player_selection, 'HUSTLE PLAYS'):.1f}")
    col3.write(f"Offensive Rebounds Allowed (per game): {average_stat(player_selection, 'O-REB ALLOW'):.1f}")
    

# Sidebar information
