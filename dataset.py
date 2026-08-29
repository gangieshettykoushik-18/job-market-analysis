import kagglehub
import pandas as pd
import os

path = kagglehub.dataset_download(
    "ravindrasinghrana/job-description-dataset"
)

print("Dataset Path:", path)

files = os.listdir(path)

print("\nFiles:")
print(files)

csv_file = os.path.join(path, files[0])

df = pd.read_csv(csv_file, nrows=10000)
print("Dataset Loaded Successfully!")

print("Duplicates:")
print(df.duplicated().sum())

print("\nTop Roles:")
print(df["Role"].value_counts().head(10))

print("\nTop Locations:")
print(df["location"].value_counts().head(10))
print("\nDataset Loaded Successfully!")
print("\nShape:")
print(df.shape)
print("\nColumns:")
print(df.columns)
print("\nFirst 5 Rows:")
print(df.head())
print("\nFirst 5 Rows:")
print(df.head())
print("\nShape:")
print(df.shape)
print("\nColumns:")
print(df.columns)
print(df.info())
print(df.isnull().sum())
print("Duplicate Rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()

df = df.fillna("Unknown")

print("Cleaning Completed")
print("\nTop 10 Roles")
print(df["Role"].value_counts().head(10))

print("\nTop 10 Locations")
print(df["location"].value_counts().head(10))
import matplotlib.pyplot as plt

top_roles = df["Role"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_roles.plot(kind="bar")

plt.title("Top 10 Job Roles")
plt.xlabel("Role")
plt.ylabel("Number of Jobs")

plt.tight_layout()
plt.show()
print(df["skills"].head())
print(df["Role"].value_counts().head(50))

print(df["Company"].value_counts().head(20))

df.to_csv("cleaned_jobs.csv", index=False)
