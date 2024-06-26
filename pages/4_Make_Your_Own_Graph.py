import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt

@st.cache_data
def load_data(csv):
    df= pd.read_csv(csv)
    return df

salary = load_data('data/City_of_Charlotte_Employee_Salaries.csv')
salary = salary.drop(['OBJECTID', 'Name', 'Unit'], axis=1)
st.sidebar.header("Pick two variables for your scatterplot")

x_val = st.sidebar.selectbox("Pick your x-axis",salary.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y-axis",salary.select_dtypes(include=np.number).columns.tolist())

scatter = alt.Chart(salary, title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    tooltip=[x_val,y_val]).configure(background='#0000')

st.altair_chart(scatter, use_container_width=True)