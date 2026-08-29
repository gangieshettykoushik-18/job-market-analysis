import pandas as pd

df = pd.read_csv("cleaned_jobs.csv")

print("Total Jobs:", len(df))
print("Total Companies:", df["Company"].nunique())
print("Total Locations:", df["location"].nunique())
print("Total Roles:", df["Role"].nunique())