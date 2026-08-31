# 📊 AI-Powered Job Market Analytics Platform

An interactive **Job Market Analytics Platform** built using **Python, Pandas, Matplotlib, and Streamlit** to analyze job-market data and extract meaningful insights about job roles, salaries, companies, locations, and hiring demand.

The project transforms raw job-listing data into an interactive analytics dashboard that helps users understand current job-market patterns and salary trends.

---

## 🚀 Project Overview

The job market contains a large amount of information about available positions, companies, locations, roles, and salaries. However, raw job-listing data can be difficult to interpret directly.

This project addresses that problem by performing data processing and analysis on job-market data and presenting the results through an interactive **Streamlit dashboard**.

The platform allows users to explore:

* 📌 Most in-demand job roles
* 📍 Top hiring locations
* 🏢 Companies hiring across different locations
* 💰 Average salaries for different roles
* 📊 Overall dataset statistics
* 🎯 Role-based job filtering
* 💵 Estimated salary for a selected role
* 📈 Salary distribution

---

## 🎯 Objectives

The main objectives of this project are:

1. Analyze job-market data using Python.
2. Clean and prepare job-listing data for analysis.
3. Identify the most common job roles.
4. Identify locations with the highest number of job opportunities.
5. Analyze salary ranges and calculate average salaries.
6. Compare salaries across different job roles.
7. Build an interactive dashboard for exploring job-market insights.
8. Provide a simple role-based salary estimation feature.

---

## 🛠️ Technologies Used

| Technology     | Purpose                                |
| -------------- | -------------------------------------- |
| **Python**     | Core programming and data analysis     |
| **Pandas**     | Data cleaning, processing and analysis |
| **Matplotlib** | Data visualization                     |
| **Streamlit**  | Interactive web dashboard              |
| **CSV**        | Job-market dataset storage             |

---

## 📂 Project Structure

```text
job-market-analysis/
│
├── 📊 Figure_1.png
├── 📊 Figure_2.png
│
├── 🐍 checkdataset.py
├── 🐍 cleaned_jobs.csv
├── 🐍 dashboard.py
├── 🐍 dashboard_metrics.py
├── 🐍 data_roles.py
├── 🐍 dataset.py
├── 🐍 readdataset.py
├── 🐍 salary_analysis.py
├── 🐍 testpandas.py
│
└── 📄 README.md
```

---

## 🔍 Data Analysis

The project uses a cleaned job-market dataset containing information such as:

* Job Role
* Company
* Location
* Salary Range

The dataset is loaded using Pandas and processed before being displayed in the dashboard.

The application reads the dataset using:

```python
pd.read_csv("cleaned_jobs.csv")
```

---

## 📊 Dashboard Features

### 1. Dataset KPIs

The dashboard provides important high-level statistics including:

* Total number of jobs
* Number of companies
* Number of locations
* Number of job roles

These metrics provide an overview of the dataset.

---

### 2. 🎯 Job Role Filter

Users can select a specific job role from an interactive dropdown.

The dashboard then displays the number of job listings available for the selected role.

---

### 3. 📌 Top 10 Job Roles

The platform identifies and visualizes the **10 most frequently occurring job roles** in the dataset.

This helps identify which positions have the highest representation in the analyzed job market.

---

### 4. 📍 Top 10 Locations

The dashboard analyzes job locations and displays the **10 locations with the highest number of job listings**.

This can help identify major hiring locations represented in the dataset.

---

### 5. 💰 Salary Analysis

Salary ranges are processed into:

* Minimum Salary
* Maximum Salary
* Average Salary

The average salary is calculated using:

```text
Average Salary = (Minimum Salary + Maximum Salary) / 2
```

The dashboard then calculates the average salary for each job role.

---

### 6. 💸 Highest-Paying Roles

The application groups jobs by role and calculates the average salary for each role.

The **top 10 highest-paying roles** are then displayed using a bar chart.

This provides a quick comparison of salary levels across different job positions.

---

### 7. 💵 Salary Predictor

The dashboard includes a simple **role-based salary estimation feature**.

Users select a job role and the application calculates the mean average salary of jobs belonging to that role.

The result is displayed as an estimated salary for the selected role.

> **Note:** This is a statistical salary estimate based on the available dataset, not a machine-learning prediction model.

---

### 8. 📈 Salary Distribution

The application also displays the distribution of average salaries using a histogram.

This helps understand how salaries are distributed across the analyzed job listings.

---

## ⚙️ How the Project Works

```text
Raw Job Market Data
        ↓
Data Cleaning & Preparation
        ↓
Cleaned Jobs Dataset
        ↓
Pandas Data Processing
        ↓
Salary & Job Role Analysis
        ↓
Matplotlib Visualizations
        ↓
Streamlit Dashboard
        ↓
Interactive Job Market Insights
```

---

## 🧹 Data Processing

The project performs several data-processing operations before visualization.

These include:

* Reading CSV data
* Checking dataset structure
* Cleaning job-market data
* Processing salary ranges
* Separating minimum and maximum salaries
* Calculating average salaries
* Counting unique companies
* Counting unique locations
* Counting unique job roles
* Grouping jobs by role
* Ranking job roles and locations

---

## 📈 Key Insights

The platform is designed to help answer questions such as:

* Which job roles appear most frequently?
* Which locations have the highest number of opportunities?
* Which roles have higher average salaries?
* How are salaries distributed across job listings?
* How many companies are represented in the dataset?
* What is the estimated average salary for a particular role?

---

## ▶️ How to Run the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/gangieshettykoushik-18/job-market-analysis.git
```

### Step 2: Open the project

```bash
cd job-market-analysis
```

### Step 3: Install the required libraries

```bash
pip install pandas matplotlib streamlit
```

### Step 4: Run the Streamlit dashboard

```bash
streamlit run dashboard.py
```

The dashboard will open in your browser.

---

## 🖥️ Dashboard

The Streamlit application provides an interactive interface where users can explore job-market statistics, job roles, locations, salary information, and role-based salary estimates.

---

## 📊 Visualizations

The project contains visualizations for:

* Top job roles
* Top hiring locations
* Highest-paying job roles
* Salary distribution

---

## 💡 Future Enhancements

The project can be further improved by adding:

* 🤖 Machine-learning-based salary prediction
* 🔎 Job recommendation system
* 🧠 NLP-based skill extraction
* 📌 Skill-demand analysis
* 📊 Advanced interactive Plotly dashboards
* 🌍 Geographic job-market visualization
* 📈 Job-market trend analysis over time
* 🎓 Fresher-friendly job analysis
* 🏢 Company-wise hiring analysis
* 🎯 Resume-to-job matching
* ☁️ Deployment using Streamlit Cloud

---

## 📚 Skills Demonstrated

This project demonstrates practical experience in:

* Python Programming
* Data Cleaning
* Exploratory Data Analysis
* Data Manipulation
* Data Visualization
* Statistical Analysis
* Pandas
* Matplotlib
* Streamlit
* Dashboard Development
* Data-driven Problem Solving

---

## 👨‍💻 Author

**Koushik Gangishetti**

B.Tech – Artificial Intelligence & Data Science

GitHub:
https://github.com/gangieshettykoushik-18

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is available for educational and portfolio purposes.
