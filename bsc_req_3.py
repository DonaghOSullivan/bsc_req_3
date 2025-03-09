#analysis


import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

import subprocess

process = subprocess.Popen([
    "streamlit", "run", "bsc_req_3.py",
    "--server.port", "157",
    "--server.headless", "true"
])



file_path = 'clean.csv'
data = pd.read_csv(file_path)


st.title("Football Statistics Information System")
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



    plt.figure(figsize=(10, 6))
    plt.bar(team_data['Player'], team_data['Actual Goals'], color='green')
    plt.title("Actual Goals by Player")
    plt.xlabel("Player")
    plt.ylabel("Actual Goals")
    plt.xticks(rotation=45)
    st.pyplot(plt) 

elif selected_stat == 'Most Expected Goals':
    top_player = team_data.loc[team_data['Expected Goals (xG)'].idxmax()]
    st.subheader("Most Expected Goals")
    st.write("Player: " + top_player['Player'] + " - Expected Goals: " + str(top_player['Expected Goals (xG)']))


    plt.figure(figsize=(10, 6))
    plt.bar(team_data['Player'], team_data['Expected Goals (xG)'], color='green')
    plt.title("Expected Goals by Player")
    plt.xlabel("Player")
    plt.ylabel("Expected Goals (xG)")
    plt.xticks(rotation=45)
    st.pyplot(plt) 

elif selected_stat == 'Biggest Difference':
    team_data['Abs Difference'] = team_data['Goal Difference'].abs()
    top_player = team_data.loc[team_data['Abs Difference'].idxmax()]
    st.subheader("Biggest Difference in Goals")
    st.write("Player: " + top_player['Player'] + " - Goal Difference: " + str(top_player['Goal Difference']))


    plt.figure(figsize=(10, 6))
    plt.bar(team_data['Player'], team_data['Goal Difference'], color='green')
    plt.title("Goal Difference by Player")
    plt.xlabel("Player")
    plt.ylabel("Goal Difference")
    plt.xticks(rotation=45)
    st.pyplot(plt) 
