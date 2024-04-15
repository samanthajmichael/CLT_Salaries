import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Trend of Average Salary Over the Years')

@st.cache_data
def load_data(csv):
    df= pd.read_csv(csv)
    return df

salary = load_data('data/City_of_Charlotte_Employee_Salaries.csv')
salary = salary.drop(['OBJECTID', 'Name', 'Unit'], axis=1)

# Group the data by 'Year' and calculate the average salary for each year
average_salary_yearly = salary.groupby('Year')['Annual_Rt'].mean().reset_index()

# Plotting the trend of average salary over the years
plt.figure(figsize=(10, 6))
sns.lineplot(data=pd.DataFrame(average_salary_yearly), x='Year', y='Annual_Rt', marker='o')
plt.xlabel('Year')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(plt)