from operator import index
import streamlit as st
import plotly.express as px
from pycaret.regression import setup, compare_models, pull, save_model, load_model
import pandas_profiling
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os 

if os.path.exists('./data/dataset.csv'): 
    df = pd.read_csv('data/dataset.csv', index_col=None)

with st.sidebar: 
    st.image("./images/AUTO.png")
    st.title("Auto L33TH ML")
    choice = st.radio("Navigation", ["Upload","Profiling","Modeling", "Download"])
    st.info("This machine learning application helps you build and explore your data.")

if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

if choice == "Profiling": 
    st.title("Exploratory Data Analysis")
    profile_df = df.profile_report()
    st_profile_report(profile_df)

if choice == "Modeling": 
    chosen_target = st.selectbox('Choose the Target Column', df.columns)
    if st.button('Run Modeling'): 
        setup(df, target=chosen_target, silent=True)
        setup_df = pull()
        st.dataframe(setup_df)
        best_model = compare_models()
        compare_df = pull()
        st.dataframe(compare_df)
        save_model(best_model, 'l33th_auto_model')

if choice == "Download": 
    with open('l33th_auto_model.pkl', 'rb') as f: 
        st.download_button('Download Model', f, file_name="l33th_auto_model.pkl")