import streamlit as st
import pandas as pd

st.title("Charlotte Men's Club Basketball 2023-24 Stats App")

# Reading in the data from local desktop 
df = pd.read_csv('./mcbb3_stats.csv')
# Cleaning data that was not needed from csv 
df['2FG %'] = df['2FG %'].str.strip('%')
df['3FG %'] = df['3FG %'].str.strip('%')
df['TFG %'] = df['TFG %'].str.strip('%')
df['FT %'] = df['FT %'].str.strip('%')
df = df.drop(range(17, df.shape[0], 18))


# Selecting a player
player_selection = st.selectbox(
    "Select a player to view per game averages or season highs",
    df['Name'].unique(),
    help="Select a player from the list"
)


# Visual color for buttons 
st.markdown('<style>div.row-widget.stButton > button {font-weight: bold; color: #ff5733; border: 2px solid black;}</style>', unsafe_allow_html=True)

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
with col1:
    if st.button("Calculate Averages"):
        st.write(f"##### **Averages:**")
        st.write(f"PPG: {average_stat(player_selection, 'PTS'):.1f}")
        st.write(f"RPG: {average_stat(player_selection, 'TOTAL REB'):.1f}")
        st.write(f"APG: {average_stat(player_selection, 'AST'):.1f}")
        st.write(f"BPG: {average_stat(player_selection, 'BLK'):.1f}")
        st.write(f"SPG: {average_stat(player_selection, 'STL'):.1f}")
        st.write(f"TOPG: {average_stat(player_selection, 'TOV'):.1f}")
        col2.write(f"##### **Shooting Splits:**")
        col2.write(f"2FG: {average_stat(player_selection, '2FG %'):.1f}%")
        col2.write(f"3FG: {average_stat(player_selection, '3FG %'):.1f}%")
        col2.write(f"TFG: {average_stat(player_selection, 'TFG %'):.1f}%")
        col2.write(f"FT: {average_stat(player_selection, 'FT %'):.1f}%")
        col2.write(f"##### **Miscellaneous Stats:**")
        col2.write(f"Average Game Score: {average_stat(player_selection, 'G-SCORE'):.1f}")
        col2.write(f"Hustle Plays (per game): {average_stat(player_selection, 'HUSTLE PLAYS'):.1f}")
        #col3.write(f"Offensive Rebounds Allowed (per game): {average_stat(player_selection, 'O-REB ALLOW'):.1f}")
    
# function (4) to calculate season highs
def max_stat(player_name, stat):
    player_data = df[df['Name'].str.lower() == player_name.lower()]
    valid_data = player_data[pd.to_numeric(player_data[stat], errors='coerce').notna()]
    max_value = valid_data[stat].astype(float).max()
    game_index = valid_data[valid_data[stat].astype(float) == max_value].index[0]
    game_info = df.loc[game_index, ['VERSUS', 'DATE']]
    return max_value, game_info['VERSUS'], game_info['DATE']

def season_high(player_name, stat, stat2, stat3, stat4, stat5):
    max_value, versus, date = max_stat(player_name, stat)
    max_value2, versus2, date2 = max_stat(player_name, stat2)
    max_value3, versus3, date3 = max_stat(player_name, stat3)
    max_value4, versus4, date4 = max_stat(player_name, stat4)
    max_value5, versus5, date5 = max_stat(player_name, stat5)
    return max_value, versus, date, max_value2, versus2, date2, max_value3, versus3, date3, max_value4, versus4, date4, max_value5, versus5, date5


# Display season highs
if player_selection:
        with col3:
            if st.button("Display Season Highs", key="display_season_highs_button"):
                max_value, versus, date, max_value2, versus2, date2, max_value3, versus3, date3, max_value4, versus4, date4, max_value5, versus5, date5 = season_high(player_selection, 'PTS', 'AST', 'TOTAL REB', 'STL', 'BLK')
                col1.write(f"#### **{player_selection} Season Highs:**")
                col1.write(f"**Points:** {max_value:.0f} vs. {versus} on {date}")
                col1.write(f"**Assists:** {max_value2:.0f} vs. {versus2} on {date2}")
                col1.write(f"**Rebounds:** {max_value3:.0f} vs. {versus3} on {date3}")
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write(f"**Steals:** {max_value4:.0f} vs. {versus4} on {date4}")
                col2.write(f"**Blocks:** {max_value5:.0f} vs. {versus5} on {date5}")


# Sidebar information
st.sidebar.markdown("<h1 style='text-align: center; font-size: 24px;'>We OVER Me</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size: 16px; text-align: center;'>The motto for the Charlotte Men's Club Basketball Team has stuck for the past two seasons, and the team has well fulfilled the meaning.</p>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size: 16px; text-align: center;'>Boasting a 24-3 Record and Ranked Top 10 in the National Club Basketball Rankings, This Team Has Made Its Mark.</p>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size: 16px; text-align: center;'>This Is a Comprehensive Stats App to See the Numbers View of the Team. Created by Daivik Nambiar.</p>", unsafe_allow_html=True)
st.sidebar.image("./Charlotte_49ers_logo.svg.png", use_column_width=True)  
   
# Visual line to divide the two sections    
st.markdown('<hr style="border: 2px solid #ddd;">', unsafe_allow_html=True)
 
# Team Stats Section 
st.write("### Team Stats")
st.write("<small> Click the buttons below each line to view box scores. **(Note: Some box scores may be incomplete)**")

charlotte_stats = df[df['Name'] == 'CHARLOTTE']
opponent_stats = df[df['Name'] == 'Opponent']

# Determine the minimum length of the two DataFrames
min_length = min(len(charlotte_stats), len(opponent_stats))

for i in range(min_length):
    charlotte_row = charlotte_stats.iloc[i]
    charlotte_name = charlotte_row['Name']
    charlotte_pts = charlotte_row['PTS']
    date = charlotte_row['DATE']
    opponent_row = opponent_stats.iloc[i]
    opponent_name = opponent_row['VERSUS']
    opponent_pts = opponent_row['PTS']
    
    total_rows = len(df)

    # Display game results and buttons
    for i in range(total_rows // 17 + 1): 
        start_index = i * 17
        end_index = (i + 1) * 17
        
        if end_index > total_rows:
            end_index = total_rows
        
        if start_index < total_rows:
            charlotte_row = charlotte_stats.iloc[i]
            charlotte_name = charlotte_row['Name']
            charlotte_pts = charlotte_row['PTS']
            date = charlotte_row['DATE']
            opponent_row = opponent_stats.iloc[i]
            opponent_name = opponent_row['VERSUS']
            opponent_pts = opponent_row['PTS']
            
            # Display the game result
            st.write(f"{date} - **{charlotte_name}**: {charlotte_pts}, **{opponent_name}**: {opponent_pts}")
            
            # Add a button for this game result
            if st.button("Details", key=f"button{i + 1}"):
                st.write(df.iloc[start_index:end_index])




