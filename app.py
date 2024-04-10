import streamlit as st
import pandas as pd

# Load the CSV file
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['2FG %'] = df['2FG %'].str.strip('%')
    df['3FG %'] = df['3FG %'].str.strip('%')
    df['TFG %'] = df['TFG %'].str.strip('%')
    df['FT %'] = df['FT %'].str.strip('%')
    df = df.drop(range(17, df.shape[0], 18))
    return df

# Function to compute averages
def average_stat(player_name, stat, df):
    player_data = df[df['Name'].str.lower() == player_name.lower()]
    valid_data = player_data[pd.to_numeric(player_data[stat], errors='coerce').notna()]
    return valid_data[stat].astype(float).mean()

def main():
    st.title('Basketball Player Stats')

    # Load data (assuming your file is named 'mcbb_stats.csv')
    file_path = 'mcbb_stats.csv'
    df = load_data(file_path)

    st.write('### Data Overview')
    st.write(df)

    # Provided name options
    name_options = ['Tre Clemons', 'Anthony Franchi', 'Drew Moore', 'Trian Barnes', 'JJ Sciba',
                    'Jourdan Watkins', 'Trevor Kelly', 'Sos Igbnigie', 'Tyler Druskis', 'Tevin Jessup',
                    'Zach Friday', 'Caleb Tillis', 'Meelad Doroodchi', 'Cole Strand', 'Max Reid']

    # Dropdown to select player names
    selected_name = st.selectbox('Select Player Name', name_options)

    st.write('### Averages for {}'.format(selected_name.title()))
    st.write(f"{selected_name.title()} averages {average_stat(selected_name, 'PTS', df):.1f} PTS per game")
    st.write(f"{selected_name.title()} averages {average_stat(selected_name, 'TOTAL REB', df):.1f} REB per game")
    st.write(f"{selected_name.title()} averages {average_stat(selected_name, 'AST', df):.1f} AST per game")
    st.write(f"{selected_name.title()} averages {average_stat(selected_name, 'STL', df):.1f} STL per game")
    st.write(f"{selected_name.title()} averages {average_stat(selected_name, 'BLK', df):.1f} BLK per game")
    st.write(f"{selected_name.title()} averages {average_stat(selected_name, 'TOV', df):.1f} TOV per game")

if __name__ == "__main__":
    main()
