import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# App Title
st.title("Solar Radiation Analysis - Benin Malanville")

# File Uploader
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])
if uploaded_file:
    # Load Dataset
    df = pd.read_csv(uploaded_file)

    # Show Data Preview
    st.write("Dataset Preview:")
    st.dataframe(df.head())

    # Visualization: GHI Distribution
    st.subheader("Global Horizontal Irradiance (GHI) Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['GHI'], kde=True, color="skyblue", ax=ax)
    st.pyplot(fig)
