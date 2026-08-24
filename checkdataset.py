import os

path = r"C:\Users\hp\.cache\kagglehub\datasets\ravindrasinghrana\job-description-dataset\versions\1"

print("Files in dataset:")

for file in os.listdir(path):
    print(file)