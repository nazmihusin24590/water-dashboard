# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import urllib

# Function to load data from GitHub
@st.cache  # Cache data for faster reload
def load_data():
    url = 'https://raw.githubusercontent.com/your_username/your_repository/main/Data.csv'
    df = pd.read_csv(url)
    return df

# Function to plot line chart
def plot_line_chart(df, x_col, y_col, title, x_label, y_label):
    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col])
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    st.pyplot(fig)

# Function to plot bar chart
def plot_bar_chart(df, x_col, y_col, title, x_label, y_label):
    fig, ax = plt.subplots()
    ax.bar(df[x_col], df[y_col])
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    st.pyplot(fig)

# Main function
def main():
    st.title('Water Quality and Discharge Dashboard')

    # Load data
    df = load_data()

    # Display the dataframe
    st.subheader('Data Table')
    st.write(df)

    # Line charts for pH, COD, SS
    st.subheader('Line Charts')

    plot_line_chart(df, 'Date', 'pH', 'Date vs pH', 'Date', 'pH')
    plot_line_chart(df, 'Date', 'COD', 'Date vs COD', 'Date', 'COD')
    plot_line_chart(df, 'Date', 'SS', 'Date vs SS', 'Date', 'SS')

    # Bar chart for volume of discharge
    st.subheader('Bar Chart for Volume of Discharge')
    plot_bar_chart(df, 'Date', 'Volume of discharge (m3)', 'Date vs Volume of Discharge', 'Date', 'Volume (m3)')

if __name__ == '__main__':
    main()
