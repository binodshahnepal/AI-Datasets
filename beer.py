import streamlit as st
import pandas as pd
from joblib import load
from sklearn.preprocessing import StandardScaler

# Load the model
model = load('beer.joblib')

# Define the title of the app
st.title('Beer Consumption Prediction')

# Create input fields for user to enter data
st.header('Enter the following details:')
year = st.number_input('Year', min_value=2000, max_value=2100, step=1)
month = st.number_input('Month', min_value=1, max_value=12, step=1)
day_of_week = st.number_input('Day of Week', min_value=0, max_value=6, step=1)
temperatura_media = st.number_input('Temperatura Media (C)')
temperatura_minima = st.number_input('Temperatura Minima (C)')
temperatura_maxima = st.number_input('Temperatura Maxima (C)')
precipitacao = st.number_input('Precipitacao (mm)')
final_de_semana = st.selectbox('Final de Semana', [0, 1])

# Create a predict button
if st.button('Predict'):
    # Create a dataframe with the user input
    data = {
        'Year': [year],
        'Month': [month],
        'Day of Week': [day_of_week],
        'Temperatura Media (C)': [temperatura_media],
        'Temperatura Minima (C)': [temperatura_minima],
        'Temperatura Maxima (C)': [temperatura_maxima],
        'Precipitacao (mm)': [precipitacao],
        'Final de Semana': [final_de_semana]
    }
    input_data = pd.DataFrame(data)

    # Drop the 'Year' column if it was dropped during model training
    input_data = input_data.drop(columns=['Year'])

    # Predict beer consumption
    prediction = model.predict(input_data)
    st.subheader(f'Predicted Beer Consumption: {prediction[0]:.2f} liters')
