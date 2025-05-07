import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("vehicles_us.csv")
df['vehicle_age'] = 2025 - df['model_year']

st.header("🚗 Vehicle Listings Dashboard")

# Checkbox that changes chart behavior
exclude_expensive = st.checkbox("Exclude vehicles over $50,000")

if exclude_expensive:
    filtered_df = df[df['price'] <= 50000]
else:
    filtered_df = df

# Histogram: Vehicle Age
st.subheader("Distribution of Vehicle Age")
fig1 = px.histogram(filtered_df, x='vehicle_age', nbins=30,
                    title='Distribution of Vehicle Age',
                    labels={'vehicle_age': 'Vehicle Age (Years)'})
st.plotly_chart(fig1)

# Scatterplot: Price vs Odometer
st.subheader("Price vs Odometer by Condition")
fig2 = px.scatter(filtered_df, x='odometer', y='price', color='condition',
                  title='Price vs Odometer by Condition',
                  labels={'odometer': 'Mileage', 'price': 'Price ($)'})
st.plotly_chart(fig2)
