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

df = pd.read_csv(csv_file)
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