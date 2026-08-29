import pandas as pd

df = pd.read_csv("cleaned_jobs.csv")

data_roles = df[
    df["Role"].str.contains(
        "Data|Analyst|Scientist|Business Intelligence",
        case=False,
        na=False
    )
]

print(data_roles["Role"].value_counts().head(20))