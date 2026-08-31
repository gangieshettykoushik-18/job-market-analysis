import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Job Market Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv("cleaned_jobs.csv")

# -----------------------------
# SALARY PROCESSING
# -----------------------------

salary_split = (
    df["Salary Range"]
    .str.replace("$", "", regex=False)
    .str.replace("K", "", regex=False)
    .str.split("-", expand=True)
)

df["Min Salary"] = salary_split[0].astype(int)
df["Max Salary"] = salary_split[1].astype(int)

df["Avg Salary"] = (
    df["Min Salary"] + df["Max Salary"]
) / 2

# -----------------------------
# TITLE
# -----------------------------

st.title("📊 Job Market Analytics Dashboard")

# -----------------------------
# KPI CARDS
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Jobs", len(df))

with col2:
    st.metric("Companies", df["Company"].nunique())

with col3:
    st.metric("Locations", df["location"].nunique())

with col4:
    st.metric("Roles", df["Role"].nunique())

# -----------------------------
# ROLE FILTER
# -----------------------------

st.header("🎯 Role Filter")

selected_role = st.selectbox(
    "Select Role",
    sorted(df["Role"].dropna().unique()),
    key="role_filter"
)

filtered_df = df[df["Role"] == selected_role]

st.write(f"Selected Role: **{selected_role}**")
st.write(f"Number of Jobs Found: **{len(filtered_df)}**")

# -----------------------------
# TOP JOB ROLES
# -----------------------------

st.header("📌 Top 10 Job Roles")

fig1, ax1 = plt.subplots(figsize=(10, 5))

df["Role"].value_counts().head(10).plot(
    kind="bar",
    color="skyblue",
    ax=ax1
)

ax1.set_xlabel("Role")
ax1.set_ylabel("Count")

st.pyplot(fig1)

# -----------------------------
# TOP LOCATIONS
# -----------------------------

st.header("📍 Top 10 Locations")

fig2, ax2 = plt.subplots(figsize=(10, 5))

df["location"].value_counts().head(10).plot(
    kind="bar",
    color="orange",
    ax=ax2
)

ax2.set_xlabel("Location")
ax2.set_ylabel("Count")

st.pyplot(fig2)

# -----------------------------
# TOP HIGHEST PAYING ROLES
# -----------------------------

st.header("💸 Top 10 Highest Paying Roles")

salary_role = (
    df.groupby("Role")["Avg Salary"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

fig3, ax3 = plt.subplots(figsize=(10, 5))

salary_role.plot(
    kind="bar",
    color="green",
    ax=ax3
)

ax3.set_xlabel("Role")
ax3.set_ylabel("Average Salary (K USD)")

st.pyplot(fig3)

# -----------------------------
# SALARY PREDICTOR
# -----------------------------

st.header("💰 Salary Predictor")

role_input = st.selectbox(
    "Choose Role",
    sorted(df["Role"].dropna().unique()),
    key="salary_predictor_role"
)

prediction_df = df[df["Role"] == role_input]

if len(prediction_df) > 0:

    avg_salary = prediction_df["Avg Salary"].mean()

    st.success(
        f"Estimated Salary for {role_input}: ${avg_salary:.2f}K"
    )

else:

    st.warning(
        "No salary information available."
    )

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("---")

st.success(
    "✅ AI-Powered Job Market Analytics Dashboard Running Successfully"
)
st.title("AI-Powered Job Market Analytics Platform")

st.markdown("""
This platform analyzes job market trends,
salary distributions, hiring locations,
and role demand using Data Science techniques.
""")
st.subheader("Dataset Statistics")

st.write("Total Records:", len(df))
st.write("Total Companies:", df["Company"].nunique())
st.write("Total Locations:", df["location"].nunique())
fig, ax = plt.subplots(figsize=(8,5))

df["Avg Salary"].hist(
    bins=20,
    color="skyblue"
)

st.pyplot(fig)