import plotly.express as px
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import dtreeviz
import pickle 
import warnings
import numpy as np
from sklearn.tree import plot_tree
from sklearn.ensemble import GradientBoostingClassifier

warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
data=pd.read_csv(r"D:\College\Sem 5\ML\ML Final Lab Test\fetal_health.csv")
data.replace([np.inf, -np.inf], np.nan, inplace=True)

data.dropna(inplace=True)
y=data["fetal_health"]
X=data.drop(["fetal_health"],axis=1)

def hist():
    st.markdown("<h4 style='text-align: center; color: #FFA500;'>Evaluating distributions of the features</h4>", unsafe_allow_html=True)
    hist_plot = data.hist(figsize=(20, 20), color="#483D8B")
    st.pyplot(hist_plot[0][0].get_figure())
def target():
    st.markdown("<h4 style='text-align: center; color: #FFA500;'>Target column</h4>", unsafe_allow_html=True)
    colors = ["#483D8B", "#4682B4", "#87CEFA"]
    ax = sns.countplot(data=data, x="fetal_health", palette=colors)
    ax.bar_label(ax.containers[0])
    st.pyplot(fig=ax.figure)
def violin(col):
    st.markdown("<h4 style='text-align: center; color: #FFA500;'>Histogram Data</h4>", unsafe_allow_html=True)
    fig = px.violin(data, y=col, x="fetal_health", color="fetal_health", box=True, template='plotly_dark')
    st.plotly_chart(fig)
def kde(col):
    st.markdown("<h4 style='text-align: center; color: #FFA500;'>Histogram Number of peaks</h4>", unsafe_allow_html=True)
    grid = sns.FacetGrid(data, hue="fetal_health", height=6, aspect=2)
    grid.map(sns.kdeplot, col)
    grid.add_legend()
    fig = grid.fig
    st.pyplot(fig)

def scatter(col1, col2):
    st.markdown("<h4 style='text-align: center; color: #FFA500;'>Fetal Movement Vs Utriene Contraction </h4>", unsafe_allow_html=True)
    fig = px.scatter(data, x=col1, y=col2, color="fetal_health", template='plotly_dark')
    st.plotly_chart(fig)
def corr():
    st.markdown("<h4 style='text-align: center; color: #FFA500;'>Correlation</h4>", unsafe_allow_html=True)
    cmap = sns.diverging_palette(205, 133, 63, as_cmap=True)
    cols = (["#B0E0E6", "#87CEFA", "#4682B4", "#CD853F", "#DEB887", "#FAEBD7"])
    corrmat = data.corr()
    f, ax = plt.subplots(figsize=(15, 15))
    heatmap = sns.heatmap(corrmat, cmap=cols, annot=True)
    st.pyplot(f)
def outlier():
    st.markdown("<h4 style='text-align: center; color: #FFA500;'>Boxenplots</h4>", unsafe_allow_html=True)
    colors = ["#483D8B", "#4682B4", "#87CEFA"]
    plt.figure(figsize=(20, 10))
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(data)
    boxen_plot = sns.boxenplot(data=X_scaled, palette=colors)
    plt.xticks(rotation=60)
    st.pyplot(plt)

hist()
#target()
violin('histogram_number_of_peaks')
kde('histogram_number_of_peaks')
scatter('fetal_movement','uterine_contractions')
corr()
outlier()
