from operator import index
import streamlit as st
import plotly.express as px
from pycaret.regression import setup, compare_models, pull, save_model, load_model
import pandas_profiling
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os

if os.path.exists('./dataset.csv'):
    df = pd.read_csv('dataset.csv', index_col=None)

st.set_page_config(page_title="Build0Brain", page_icon="https://i.ibb.co/CM7vxgY/2.png")

with st.sidebar: 
    st.title("AutoGenML")
    choice = st.radio("Navigation", ["Upload","Profiling"])
    st.image("https://i.ibb.co/nbrM4Ft/data-Analysis.png")
    #choice = st.radio("Navigation", ["Upload","Profiling"])
    st.info("This project application helps you build and explore your data.")

if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    st.info("The dataset must be in Excel as csv file format")
    st.image("https://i.ibb.co/JqXW2D7/image.png",width=300)
    if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)


if choice == "Profiling":
    st.title("Exploratory Data Analysis")
    profile_df = df.profile_report()
    st_profile_report(profile_df)

# if choice == "Modelling": 
#     chosen_target = st.selectbox('Choose the Target Column', df.columns)
#     if st.button('Run Modelling'): 
#         setup(df, target=chosen_target, silent=True)
#         setup_df = pull()
#         st.dataframe(setup_df)
#         best_model = compare_models()
#         compare_df = pull()
#         st.dataframe(compare_df)
#         save_model(best_model, 'best_model')

# if choice == "Download": 
#     with open('best_model.pkl', 'rb') as f: 
#         st.download_button('Download Model', f, file_name="best_model.pkl")


# import streamlit as st
# import plotly.express as px
# import pandas as pd
# import os 
# from streamlit_pandas_profiling import st_profile_report
# from ydata_profiling import ProfileReport

# # Function to safely read CSV
# def safe_read_csv(file_path):
#     try:
#         return pd.read_csv(file_path, index_col=None)
#     except Exception as e:
#         st.error(f"Error reading the CSV file: {str(e)}")
#         return None

# # Initialize session state
# if 'df' not in st.session_state:
#     st.session_state.df = None

# with st.sidebar: 
#     st.image("https://i.ibb.co/nbrM4Ft/data-Analysis.png")
#     st.title("AutoNickML")
#     choice = st.radio("Navigation", ["Upload","Profiling"])
#     st.info("This project application helps you build and explore your data.")

# if choice == "Upload":
#     st.title("Upload Your Dataset")
#     file = st.file_uploader("Upload Your Dataset")
#     if file: 
#         try:
#             st.session_state.df = pd.read_csv(file, index_col=None)
#             st.session_state.df.to_csv('dataset.csv', index=None)
#             st.success("File uploaded successfully!")
#             st.dataframe(st.session_state.df)
#         except Exception as e:
#             st.error(f"Error uploading file: {str(e)}")

# elif choice == "Profiling": 
#     st.title("Exploratory Data Analysis")
#     if st.session_state.df is not None:
#         try:
#             profile_df = ProfileReport(st.session_state.df, explorative=True)
#             st_profile_report(profile_df)
#         except Exception as e:
#             st.error(f"Error generating profile report: {str(e)}")
#     else:
#         st.warning("Please upload a dataset first.")

# # Load existing dataset if available
# if st.session_state.df is None and os.path.exists('dataset.csv'):
#     st.session_state.df = safe_read_csv('dataset.csv')
#     if st.session_state.df is not None:
#         st.success("Existing dataset loaded successfully!")

# The modeling and download sections are commented out in your original code,
# so I've left them out here. You can add them back with proper error handling
# if needed.