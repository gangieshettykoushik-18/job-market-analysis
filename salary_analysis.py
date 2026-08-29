import pandas as pd

df = pd.read_csv("cleaned_jobs.csv")

# Split salary range
salary_split = df["Salary Range"].str.replace("$", "", regex=False)\
                                 .str.replace("K", "", regex=False)\
                                 .str.split("-", expand=True)

df["Min Salary"] = salary_split[0].astype(int)
df["Max Salary"] = salary_split[1].astype(int)

df["Avg Salary"] = (
    df["Min Salary"] + df["Max Salary"]
) / 2

print(df[["Salary Range", "Avg Salary"]].head())
salary_by_role = df.groupby("Role")["Avg Salary"].mean()

print(
    salary_by_role
    .sort_values(ascending=False)
    .head(10)
)
import matplotlib.pyplot as plt

salary_by_role = (
    df.groupby("Role")["Avg Salary"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

salary_by_role.plot(kind="bar")

plt.title("Top 10 Highest Paying Roles")
plt.xlabel("Role")
plt.ylabel("Average Salary (K USD)")

plt.tight_layout()
plt.show()