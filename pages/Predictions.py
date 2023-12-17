import streamlit as st
import pickle 
import pandas as pd
from keras.models import load_model
import warnings
warnings.filterwarnings('ignore')
css_style = """
    text-align:center;
    color: #800080; 
    font-size: 1000px; 
    font-family: Arial, sans-serif; 
    
"""
css_style1 = """
    align:center;
    width: 300px;
    padding: 10px;
    border: 2px solid #333;
    background-color:rgba(0,0,0, 0.5);
    font-family: Arial, sans-serif;
    text-align: center; 
    margin: 0 auto; /* Center the box horizontally */
    color: yellow;
"""

st.markdown("<h1 style='text-align: center; color: #FFA500;'>PREDICTION</h1>", unsafe_allow_html=True)
#st.image("https://cdn-images-1.medium.com/v2/resize:fit:660/1*REUu0LJytEt6kIOFQeB0Tw.png", use_column_width=True)
feature_descriptions = {
    "Baseline value": "Baseline Fetal Heart Rate (FHR) (beats per minute)",
    "Accelerations": "Number of accelerations per second",
    "Fetal movement": "Number of fetal movements per second",
    "Uterine contractions": "Number of uterine contractions per second",
    "Light decelerations": "Number of light decelerations (LDs) per second",
    "Severe decelerations": "Number of severe decelerations (SDs) per second",
    "Prolongued decelerations": "Number of prolonged decelerations (PDs) per second",
    "Abnormal short term variability": "Percentage of time with abnormal short term variability",
    "Short term variability(mean)": "Mean value of short term variability",
    "Abnormal long term variability(percentage)": "Percentage of time with abnormal long term variability",
    "Long term variability(mean)": "Mean value of long term variability",
    "Histogram width": "Width of histogram made using all values from a record",
    "Histogram min": "Histogram minimum value",
    "Histogram max": "Histogram maximum value",
    "Histogram number of peaks": "Number of peaks in the exam histogram",
    "Histogram number of zeroes": "Number of zeros in the exam histogram",
    "Histogram mode": "Histogram mode",
    "Histogram mean": "Histogram mean",
    "Histogram median": "Histogram median",
    "Histogram variance": "Histogram variance",
    "Histogram tendency": "Histogram tendency"
}
col1, col2 = st.columns(2)
i=0
data1=pd.read_csv(r'D:\College\Sem 5\ML\ML Final Lab Test\fetal_health.csv')
data=[]
histogram_features = [feature for feature in feature_descriptions if "Histogram" in feature]
set1=["Baseline value","Abnormal short term variability","Abnormal long term variability(percentage)"]
l1=[132,0.007,0,0.008,0,0,0,16,2.4,0,19.9,117,53,170,90,137,136,138,11,1,1]
z=0
for i, (feature, description) in enumerate(feature_descriptions.items()):
    if i % 2 == 0:
        col = col1
    else:
        col = col2
    if(feature not in histogram_features):
        if feature in set1:
            value = col.number_input(f"Enter value for {feature.capitalize()}", key=f"{feature}_number_input",format="%d",value=l1[z])
            z+=1
            value = int(value)
            data.append(value)
        else:
            value = col.number_input(f"Enter value for {feature.capitalize()}", key=f"{feature}_number_input",value=l1[z])
            z+=1
            data.append(value)


with st.expander("Histogram Features"):
    for histogram_feature in histogram_features:
        value = st.number_input(f"Enter value for {histogram_feature.capitalize()}", key=f"{histogram_feature}_width",format="%d", value=l1[z])
        z+=1
        value = int(value)
        data.append(value)

df = pd.DataFrame([data],columns=data1.columns[:-1])
st.write(df)

selected_option = st.selectbox("Select a Model", ["Gradient Boosting Model", "PATE Model", "Federated Model"])
if st.button("Run Gradient Boosting", key="gradient_boosting_button", help="Click to run Gradient Boosting"):
    if(selected_option=="Gradient Boosting Model"):
        st.write("Gradient Boosting is running...")
        file = open(r"D:\College\Sem 5\ML\ML Final Lab Test\GradientBoostingClassifier (1).pkl", 'rb')
        model = pickle.load(file,encoding='latin1')
        health=model.predict(df)
        if(health[0]==1):
            prediction_text="Fetal is Normal"
        elif(health[0]==2):
            prediction_text="Fetal is in Suspect"
        elif(health[0]==3):
            prediction_text="Fetal is Pathological"
    elif(selected_option=="Federated Model"):
        st.write("Gradient Boosting is running...")
        model = load_model(r"D:\College\Sem 5\ML\ML Final Lab Test\FedaratedModel.h5")
        health=model.predict(df)
        result=health.tolist()
        class1=result.index(max(health.tolist()))
        if(class1==0):
            prediction_text="Fetal is Normal"
        elif(class1==1):
            prediction_text="Fetal is in Suspect"
        elif(class1==2):
            prediction_text="Fetal is Pathological"
    elif(selected_option=="PATE Model"):
        st.write("Gradient Boosting is running...")
        file = open(r"D:\College\Sem 5\ML\ML Final Lab Test\PATE_model.pkl", 'rb')
        model = pickle.load(file,encoding='latin1')
        health=model.predict(df)
        if(health[0]==1):
            prediction_text="Fetal is Normal"
        elif(health[0]==2):
            prediction_text="Fetal is in Suspect"
        elif(health[0]==3):
            prediction_text="Fetal is Pathological"
    st.markdown(f'<div style="{css_style1}">{prediction_text}</div>', unsafe_allow_html=True)
        