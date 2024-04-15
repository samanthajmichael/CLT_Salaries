import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Trend of Median Salary Over the Years with Mecklenburg Co Median')

@st.cache_data
def load_data(csv):
    df= pd.read_csv(csv)
    return df

salary = load_data('data/City_of_Charlotte_Employee_Salaries.csv')
salary = salary.drop(['OBJECTID', 'Name', 'Unit'], axis=1)