import streamlit as st
import pandas as pd

df = pd.read_csv("cleaned_jobs.csv")

st.title("📊 Job Market Analytics Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Jobs", len(df))

with col2:
    st.metric("Total Companies", df["Company"].nunique())

st.metric("Total Locations", df["location"].nunique())
st.metric("Total Roles", df["Role"].nunique())

st.subheader("Dataset Preview")
st.dataframe(df.head())