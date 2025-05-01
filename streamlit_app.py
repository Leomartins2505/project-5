import streamlit as st
import pandas as pd

st.title("Vehicle Dataset Explorer")

df = pd.read_csv("vehicles_us.csv")
st.write("Here's the dataset:")
st.write(df.head())
