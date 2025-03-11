#analysis


import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

#import subprocess

#process = subprocess.Popen([
#    "streamlit", "run", "bsc_req_3.py",
#    "--server.port", "157",
#    "--server.headless", "true"
#])



file_path = 'clean.csv'
data = pd.read_csv(file_path)


st.title("23/24 Premier League Shooting Statistics")
st.write("Select a club and a statistic to display.")


teams = sorted(data['Team'].unique()) 
statistics = ['Most Goals', 'Most Expected Goals', 'Biggest Difference'] 


selected_team = st.selectbox("Select Club:", teams)
selected_stat = st.selectbox("Select Statistic:", statistics)


team_data = data[data['Team'] == selected_team]


if selected_stat == 'Most Goals':
    top_player = team_data.loc[team_data['Actual Goals'].idxmax()]
    st.subheader("Most Goals")
    st.write("Player: " + top_player['Player'] + " - Goals: " + str(top_player['Actual Goals']))

    st.bar_chart(team_data.set_index('Player')['Actual Goals']) 

elif selected_stat == 'Most Expected Goals':
    top_player = team_data.loc[team_data['Expected Goals (xG)'].idxmax()]
    st.subheader("Most Expected Goals")
    st.write("Player: " + top_player['Player'] + " - Expected Goals: " + str(top_player['Expected Goals (xG)']))

    st.bar_chart(team_data.set_index('Player')['Expected Goals (xG)'])

elif selected_stat == 'Biggest Difference':
    team_data['Abs Difference'] = team_data['Goal Difference'].abs()
    top_player = team_data.loc[team_data['Abs Difference'].idxmax()]
    st.subheader("Biggest Difference in Goals")
    st.write("Player: " + top_player['Player'] + " - Goal Difference: " + str(top_player['Goal Difference']))

    st.bar_chart(team_data.set_index('Player')['Goal Difference']) 
