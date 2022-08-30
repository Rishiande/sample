import streamlit as st
import pandas as pd
st.title('my frist app')
data=pd.read_csv('cars.csv')
st.dataframe(data)
