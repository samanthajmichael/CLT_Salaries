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
# Group the data by 'Year' and calculate the average salary for each year
average_salary_yearly = salary.groupby('Year')['Annual_Rt'].median().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=pd.DataFrame(average_salary_yearly), x='Year', y='Annual_Rt', marker='o')
plt.axhline(y=79265, color='r', linestyle='-', label='Mecklenburg Co Median Income- US Census 2018-2022')  # Adding horizontal line for county median income
plt.xlabel('Year')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.legend()
plt.title('Trend of Median Salary Over the Years')
plt.tight_layout()
st.pyplot(plt)
