import streamlit as st
st.set_page_config(page_title="Dashboard",page_icon="👶🏻",layout="wide")
import pandas as pd
import streamlit.components.v1 as components
#from pandas_profiling import ProfileReport

st.markdown(
        """
        <div style="text-align: center; padding: 20px; background-color: None;">
            <h1 style="color: #FFA500; font-size: 36px; font-weight: bold;font-family: 'Arial', sans-serif;">FETAL HEALTH CLASSIFICATION</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
st.image("https://stream.org/wp-content/uploads/Scientist-Fetus-Embryo-healthy-Life-Baby-Science-Studies-900.jpg", use_column_width=True)
df=pd.read_csv("fetal_health.csv")

with st.expander(("About the Fetal health Dataset")):
    
    st.markdown((
        """
    2126 measurements extracted from cardiotocograms and classified by expert obstetricians.
    
    Cardiotocograph (CTG) is the most commonly used external monitoring system that continuously records the fetal heart rate (FHR) and uterine contraction (UC) to produce a visual display either electronically or on thermal paper.
    The main features of CTG had been extracted, which were then classified by expert obstetrician into 3 classes: "Normal", "Suspect" & "Pathological".
    """
    ))

feature_descriptions = {
    "baseline_value": "Baseline Fetal Heart Rate (FHR) (beats per minute)",
    "accelerations": "Number of accelerations per second",
    "fetal_movement": "Number of fetal movements per second",
    "uterine_contractions": "Number of uterine contractions per second",
    "light_decelerations": "Number of light decelerations (LDs) per second",
    "severe_decelerations": "Number of severe decelerations (SDs) per second",
    "prolongued_decelerations": "Number of prolonged decelerations (PDs) per second",
    "abnormal_short_term_variability": "Percentage of time with abnormal short term variability",
    "mean_value_of_short_term_variability": "Mean value of short term variability",
    "percentage_of_time_with_abnormal_long_term_variability": "Percentage of time with abnormal long term variability",
    "mean_value_of_long_term_variability": "Mean value of long term variability",
    "histogram_width": "Width of histogram made using all values from a record",
    "histogram_min": "Histogram minimum value",
    "histogram_max": "Histogram maximum value",
    "histogram_number_of_peaks": "Number of peaks in the exam histogram",
    "histogram_number_of_zeroes": "Number of zeros in the exam histogram",
    "histogram_mode": "Histogram mode",
    "histogram_mean": "Histogram mean",
    "histogram_median": "Histogram median",
    "histogram_variance": "Histogram variance",
    "histogram_tendency": "Histogram tendency",
    "fetal_health": "Encoded as 1-Normal; 2-Suspect; 3-Pathological. It is our very target column in the dataset."
}

df_feature_descriptions = pd.DataFrame(list(feature_descriptions.items()), columns=["Feature", "Description"])

# Display the DataFrame using Streamlit
with st.expander("Feature Descriptions"):
    st.dataframe(df_feature_descriptions)

st.markdown("<h1 style='text-align: center; color: #FFA500;'>DATASET</h1>", unsafe_allow_html=True)
st.write(df)
if st.sidebar.button("DataPrep"):
    st.markdown("<h1 style='text-align: center; color: #FFA500;'>DATA PREP</h1>", unsafe_allow_html=True)
    st.components.v1.html(open("fetal_health_report.html", 'r').read(),height=800,width=1000, scrolling=True)

