import streamlit as st
import pandas as pd

st.title('City of Charlotte Employee Salaries')

@st.cache_data
def load_data(csv):
    df= pd.read_csv(csv)
    return df

salary = load_data('data/City_of_Charlotte_Employee_Salaries.csv')
salary = salary.drop(['OBJECTID', 'Name', 'Unit'], axis=1)

st.dataframe(salary, use_container_width=True)
st.write('Raw data procured from City of Charlotte Open Data Portal')