import pandas as pd
import json

# Load the dataset
df = pd.read_parquet("data/task_c/task_c_trial.parquet")

# Load label mapping
with open("data/task_c/id_to_label.json", "r") as file:
    id_to_label = json.load(file)

print("Dataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 3 rows:")
print(df.head(3))

print("\nLabel mapping:")
print(id_to_label)

print("\nLabel distribution:")
print(df["label"].value_counts())

print("\nCode sample:")
print(df["code"].iloc[0])

print("\nLanguage distribution:")
print(df["language"].value_counts())

print("\nGenerator distribution:")
print(df["generator"].value_counts().head(20))

print("\nSamples per label:")
print(df.groupby(["label", "language"]).size())

# Calculate number of characters in each code sample
df["code_length"] = df["code"].str.len()

print("\nCode length statistics:")
print(df["code_length"].describe())