import pickle
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report 
from sklearn.metrics import classification_report as cr
import matplotlib.pyplot as plt
import plotly.express as px
from yellowbrick.classifier.classification_report import classification_report
from yellowbrick.classifier import ClassificationReport
from sklearn.metrics import roc_curve, auc,confusion_matrix
import plotly.express as px
from mlxtend.plotting import plot_confusion_matrix
from tensorflow.keras.models import load_model


dataset = pd.read_csv("fetal_health.csv")


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = cr(y_test, y_pred,output_dict=True)
    return accuracy, report




st.write("<h1 style='text-align: center;color:  #FFA500;'>Fetal Health Model Evaluation</h1>", unsafe_allow_html=True)


y = dataset["fetal_health"]
X = dataset.drop(columns=["fetal_health"])  # Replace "target_column" with the actual column name


with open("GradientBoostingClassifier (1).pkl", "rb") as model_file:
    models = pickle.load(model_file)
with open("PATE_model.pkl", "rb") as model_file:
    pate_models = pickle.load(model_file)
#fl_models = load_model(r"D:\College\Sem 5\ML\ML Final Lab Test\FedaratedModel.h5")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

st.sidebar.title("Select Model")
list_models=["Gradient Boosting","With PATE"]
selected_model = st.sidebar.selectbox("Select a model", list_models)
#image_path = "D:/College/Sem 5/ML/classification_report.png"



if st.button("Evaluate"):
    st.write(f"**Selected Model:** {selected_model}")
    if(selected_model=="Gradient Boosting"):
        model=models
    elif(selected_model=="With PATE"):
        model=pate_models
    

    accuracy, report = evaluate_model(model, X_test, y_test)
    
    y_pred = model.predict(X_test)
    #st.pyplot(ROCAUC(model, classes=[0,1]))
    
  

    st.write(f"**Accuracy:** {accuracy}")
    st.write("**Classification Report:**")

    average_report_df = pd.DataFrame(report).transpose()

    metrics = ['precision', 'recall', 'f1-score']
    st.write(average_report_df)

    st.write("**Metrics Plot:**")
    fig = px.bar(average_report_df, x=average_report_df.index, y=metrics,
            labels={'index': 'Classes', 'value': 'Metrics'},
            title='Metrics for Two Classes',
            color_discrete_sequence=['#FFC3A0', '#A0FFC3', '#C3A0FF'])  # Color for bars

    fig.update_xaxes(title_font=dict(size=14))
    fig.update_yaxes(title_font=dict(size=14))
    fig.update_layout(showlegend=True)
    st.plotly_chart(fig)
    fig, ax = plot_confusion_matrix(conf_mat=confusion_matrix(y_test,y_pred), figsize=(2, 2), cmap=plt.cm.Blues)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    #plt.title('Confusion Matrix', fontsize=18)
    st.pyplot(fig)
    
   



        
    









