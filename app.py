import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("vehicles_us.csv")

# Add a derived column for vehicle age
df['vehicle_age'] = 2025 - df['model_year']

# App title
st.header("🚗 Vehicle Listings Dashboard")

# Checkbox to toggle raw data display
if st.checkbox("Show raw data"):
    st.write(df)

# Histogram: Vehicle Age
st.subheader("Histogram: Vehicle Age of Listings")
fig_hist = px.histogram(df, x='vehicle_age', nbins=30,
                        title="Distribution of Vehicle Age",
                        labels={'vehicle_age': 'Vehicle Age (Years)'})
st.plotly_chart(fig_hist)

# Scatter Plot: Price vs Odometer
st.subheader("Scatter Plot: Price vs Odometer by Condition")
fig_scatter = px.scatter(df, x='odometer', y='price', color='condition',
                         title="Price vs Odometer Colored by Condition",
                         labels={'odometer': 'Mileage', 'price': 'Price ($)'})
st.plotly_chart(fig_scatter)
