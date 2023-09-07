


import pickle
import streamlit as st 
from PIL import Image
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("tableau_file.csv")
def load_data(uploaded_file):
    
    df = None
    try:
        # Try reading as CSV
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        try:
               
            # Try reading as Excel
            df = pd.read_excel(uploaded_file)
        except Exception as e:
            st.error(f"Error loading data: {e}")

    return df

st.sidebar.header('Visualisation using Excel/Tableau/Power BI/Automated EDA App')
with st.sidebar:
    st.subheader('Excel Dashboard')
    st.write('[How do average weight, age, and height vary across different obesity classes when filtered by gender, and what patterns or correlations emerge from these metrics for each gender?](https://ssu-my.sharepoint.com/:x:/r/personal/6mekik81_solent_ac_uk/Documents/Excel_Dashboard%20(1).xlsx?d=w45c3eeb6a7034eab926237ff4a95732e&csf=1&web=1&e=A7YS7F&nav=MTVfezAwMDAwMDAwLTAwMDEtMDAwMC0wMjAwLTAwMDAwMDAwMDAwMH0)')
    
    

    st.subheader('Tableau Dshboard')
    st.markdown('[How do digital habits, mobility, and physical activity, alongside factors like age, height, and weight, influence BMI and obesity levels?](https://public.tableau.com/app/profile/khadidja.mekiri4990/viz/TableauDashboard_16937747023000/Dashboard2?publish=yes)')


    st.subheader('Power BI Dashboard')
    st.write('[How do various dietary habits and consumption patterns correlate with obesity classes and overall BMI among individuals?](https://app.powerbi.com/groups/me/reports/6db1c686-fe58-45e0-8499-f5ae421966e1/ReportSection?experience=power-bi)')
  
    st.subheader('Automated EDA App')
    st.markdown('[Python Visualisation](https://autopy-jcx7mxjnys9nswfkcnbsv2.streamlit.app/)')
    

  


   #columns
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    # Add custom CSS style to position the button at the top-left corner
    st.markdown(
        """
        <style>
        .custom-button {
            position: absolute;
            top: 10px;
            left: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Use st.empty() to create an empty container at the top-left corner
    button_container = st.empty()

    # Button to be placed at the top-left corner
    if button_container.button("**Contact us**", key="costom_button"):
        
        st.write("khadidja_mek@hotmail.fr")


        
with col2:
    # Add custom CSS style to position the button at the top-left and in the middle
    st.markdown(
        """
        <style>
        .custom-button {
            position: absolute;
            top: 50%;
            left: 10px;
            transform: translateY(-50%);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Use st.empty() to create an empty container at the top-left and in the middle
    button_container = st.empty()

    # Button to be placed at the top-left and in the middle
    if button_container.button("**Help menu**", key="my_custom"):
        
        st.write("Welcome to ObeSol app!")
        
        st.write("Enter your details to predict your obesity level.")
       
        
with col3:
    # Add custom CSS style to position the button at the top-left corner
    st.markdown(
        """
        <style>
        .custom-button {
            position: absolute;
            top: 10px;
            left: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Use st.empty() to create an empty container at the top-left corner
    button_container = st.empty()
    
    if button_container.button("**Satisfaction**", key="custom"):
        st.selectbox("Rate your satisfaction (1-5)", range(1, 6))
        
with col4:
    # Add custom CSS style to position the button at the top-left corner
    st.markdown(
        """
        <style>
        .custom-button {
            position: absolute;
            top: 10px;
            left: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Use st.empty() to create an empty container at the top-left corner
    button_container = st.empty()
    if button_container.button("**The dataset**", key="Data"):
        st.write("https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition")
        
with col5:
    # Add custom CSS style to position the button at the top-left corner
    st.markdown(
        """
        <style>
        .custom-button {
            position: absolute;
            top: 10px;
            left: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Use st.empty() to create an empty container at the top-left corner
    button_container = st.empty()
    if button_container.button("**About us**", key="info"):
        st.write("Obesity Predictive System")

#display logo image
image = Image.open('logo.png')
st.image(image)
#display the title of the App
st.title('Obesity Prediction App 💎')
st.write('This application allows you to predict the obesity level.📈')

st.write('**The Dataset**')
df=pd.read_csv("tableau_file.csv")

st.write(df.head())


types = {
    'Categorical': ['Gender', 'family_history_with_overweight', 'FAVC', 'CAEC', 'SMOKE', 'SCC', 'CALC', 'MTRANS', 'Classes','FCVC', 'NCP', 'CH2O', 'FAF', 'TUE'],
    'Numerical': ['Age', 'Height', 'Weight','BMI']
}

# Initialize st.session_state.type if not present
if 'type' not in st.session_state:
    st.session_state.type = 'Categorical'  # Default to the first item in the types list


def handle_click(new_type):
    st.session_state.type = new_type


def handle_click_wo_button():
    if st.session_state.kind_of_column:
        st.session_state.type = st.session_state.kind_of_column

st.write('**EDA**')
type_of_column = st.radio('Select a column', ['Categorical', 'Numerical'], on_change=handle_click_wo_button, key='kind_of_column')


column = st.selectbox('Select a column', types[st.session_state.type])

if st.session_state.type == 'Categorical':
    dist = pd.DataFrame(df[column].value_counts()).head()
    st.bar_chart(dist)
else:
    st.table(df[column].describe())


button_spss = st.button("SPSS Visualisation")
if button_spss:
    st.write('SPSS Visualisation')

    image = Image.open('spss1.png')
    st.image(image)
    
    image = Image.open('spss2.png')
    st.image(image)
    
    image = Image.open('spss3.png')
    st.image(image)

    image = Image.open('spss4.png')
    st.image(image)

    image = Image.open('spss5.png')
    st.image(image)

button_click = st.button("WEKA Visualisation and Prediction")
if button_click:
    st.write('Weka Visualisation')
    #display image
    image = Image.open('WEKA.png')
    st.image(image)
    st.write('WEKA Results(Logistic Regression)')
    image = Image.open('WEKALR.png')
    st.image(image)




# Load model from the pkl file
with open("logistic_regression_model.pkl", 'rb') as file:
    model_pipeline_lr = pickle.load(file)


def collect_user_input():
    st.header('User Input Features')

    # Widgets for user input
    gender = st.selectbox("What is your gender", ['Female', 'Male'])
    age = st.slider("What is your age", 0, 100, 25)
    height = st.slider("What is your height (m)", 1.0, 2.5, 1.7)
    weight = st.slider("What is your Weight (kg)", 30, 150, 70)
    family_history = st.selectbox("Has a family member suffered or suffers from overweight", ["yes", "no"])
    favc = st.selectbox("Do you eat high caloric food frequently", ["yes", "no"])
    caec = st.selectbox("CAEC Do you eat any food between meals", ["no", "Sometimes", "Frequently", "Always"])
    #caec = st.selectbox("CAEC Do you eat any food between meals", ["no"/"yes"])
    smoke = st.selectbox("Do you smoke", ["yes", "no"])
    scc = st.selectbox("Do you monitor the calories you eat daily", ["yes", "no"])
    calc = st.selectbox("CALC how often do you drink alcohol", ["no", "Sometimes", "Frequently", "Always"])
    mtrans = st.selectbox("Which transportation do you usually use", ["Automobile", "Bike", "Motorbike", "Public Transportation", "Walking"])
    bmi = st.slider("What is your BMI", 10, 50, 25)
    NCP = st.slider("How many main meals do you have daily 1-Between 1 y 2/2-Three/3-More than three " , 1, 2, 3)
    FCVC = st.selectbox("Do you usually eat vegetables in your meals? 1 - Never,2- Sometimes,3- Always", ["1", "2", "3"])
    CH2O = st.selectbox("How much water do you drink daily (CH2O) 1-less than a liter/2-between 1 and 2 L/3-more than 2 L", ["1", "2", "3"])
    TUE = st.selectbox("How much time do you use technological devices daily?1- 0-2 hours/ 2- 3-5 days/ 3-more than 5 hours", ["1", "2", "3"])
    FAF = st.selectbox("How often do you have physical activity weekly?0- I do not have/1- 1 or 2days/2- 2 or 4 days/ 3- 4 or 5 days ", ["0", "1", "2", "3"])

    # Create a DataFrame from inputs
    data = {
        'Gender': gender,
        'Age': age,
        'Height': height,
        'Weight': weight,
        'family_history_with_overweight': family_history,
        'FAVC': favc,
        'CAEC': caec,
        'SMOKE': smoke,
        'SCC': scc,
        'CALC': calc,
        'MTRANS': mtrans,
        'BMI': bmi,
        'NCP': NCP,
        'FCVC': FCVC,
        'CH2O': CH2O,
        'TUE': TUE,
        'FAF': FAF
    }

    features = pd.DataFrame(data, index=[0])
    return features



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
    
    # Display user's input
    st.subheader('User Input')
    st.write(input_df)

    # If "Results" button is clicked, set the session state for the button to True
    if st.button('Results'):
        st.session_state.results_button = True

    # If the session state for "Results" is True, then show the results
    if st.session_state.results_button:
        prediction = model_pipeline_lr.predict(input_df)
        st.write("Prediction using Logistic Regression ")
        st.write(prediction[0])
        
        
        confidence_level = 98.11
        st.write('Confidence Level')
        
        if confidence_level >= 90:
            bar_color = 'green'
        elif confidence_level >= 70:
            bar_color = 'yellow'
        else:
            bar_color = 'red'

        progress_html = f"""
        <div style="position: relative; width: 100%; height: 25px; background-color: #f0f0f0; border-radius: 5px;">
            <div style="position: absolute; width: {confidence_level}%; height: 100%; background-color: {bar_color}; border-radius: 5px; transition: width 0.5s;"></div>
            <div style="position: absolute; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: black ;">
                {confidence_level:.2f}%
            </div>
        </div>
        """
        st.markdown(progress_html, unsafe_allow_html=True)










st.write("Enjoy using the app!")

st.subheader('Author👑')
st.write('**Khadidja Mekiri**' )
