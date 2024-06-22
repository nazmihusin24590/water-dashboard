import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Example GitHub raw data URL
github_url = 'https://raw.githubusercontent.com/<nazmihusin24590>/water-dashboard/blob/main/Data.csv'

# Load data from GitHub
@st.cache  # Cache data for better performance
def load_data(url):
    data = pd.read_csv(url)
    return data

df = load_data(github_url)

# Display data in Streamlit
st.title('Water Quality Discharge Dashboard')
st.write('Date, Monitoring pH, COD, SS, and Volume of Discharge')

# Show the dataframe
st.write(df)

streamlit run water_quality_dashboard.py
