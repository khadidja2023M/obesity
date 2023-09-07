import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import pickle

@st.cache
def load_data():
    return pd.read_csv("tableau_file.csv")

df = load_data()

# Initialize session states
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = 'dataset'  # Default to dataset view
if 'type' not in st.session_state:
    st.session_state.type = 'Categorical'  # Default to the first item in the types list

view_mode = st.radio('Choose View', ['dataset', 'EDA'])

if view_mode == 'dataset':
    st.write('**The Dataset**')
    st.write(df.head())
elif view_mode == 'EDA':
    types = {
        'Categorical': ['Gender', 'family_history_with_overweight', 'FAVC', 'CAEC', 'SMOKE', 'SCC', 'CALC', 'MTRANS', 'Classes', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE'],
        'Numerical': ['Age', 'Height', 'Weight', 'BMI']
    }
    st.write('**EDA**')
    st.session_state.type = st.radio('Select a column type', ['Categorical', 'Numerical'])
    column = st.selectbox('Select a column', types[st.session_state.type])

    if st.session_state.type == 'Categorical':
        dist = pd.DataFrame(df[column].value_counts()).head()
        st.bar_chart(dist)
    else:
        st.table(df[column].describe())
    
    st.subheader('Heatmap')
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", linewidths=.5, ax=ax)
    st.pyplot(fig)

button_spss = st.button("SPSS Visualisation")
if button_spss:
    st.write('SPSS Visualisation')
    for img_name in ['spss1.png', 'spss2.png', 'spss3.png', 'spss4.png', 'spss5.png']:
        image = Image.open(img_name)
        st.image(image)

button_click = st.button("WEKA Visualisation and Prediction")
if button_click:
    st.write('Weka Visualisation')
    image = Image.open('WEKA.png')
    st.image(image)
    st.write('WEKA Results(Logistic Regression)')
    image = Image.open('WEKALR.png')
    st.image(image)

# Load model from the pkl file
with open("logistic_regression_model.pkl", 'rb') as file:
    model_pipeline_lr = pickle.load(file)

def collect_user_input():
    # ... (same as you provided) ...

# Check if 'prediction_button' is in the session state:
    if 'prediction_button' not in st.session_state:
      st.session_state.prediction_button = False  # Default to not clicked

    if 'results_button' not in st.session_state:
      st.session_state.results_button = False  # Default to not clicked

    # Load model
    with open("logistic_regression_model.pkl", 'rb') as file:
      model_pipeline_lr = pickle.load(file)

    # If "Prediction" button is clicked, set the session state for the button to True
    if st.button('Logistic Regression Prediction'):
      st.session_state.prediction_button = True

# If the session state for "Prediction" is True, then show the input fields
if st.session_state.prediction_button:
    input_df = collect_user_input()  # Assume the function 'collect_user_input' collects and returns user inputs in a DataFrame
    st.subheader('User Input')
    st.write(input_df)

    # If "Results" button is clicked, set the session state for the button to True
    if st.button('Results'):
        st.session_state.results_button = True

    if st.session_state.results_button:
        prediction = model_pipeline_lr.predict(input_df)
        st.write("Prediction using Logistic Regression ")
        st.write(prediction[0])

        confidence_level = 98.11
        st.write('Confidence Level')
        # ... (same as you provided) ...

st.write("Enjoy using the app!")
st.subheader('Author👑')
st.write('**Khadidja Mekiri**')
