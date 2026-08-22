import pandas as pd
import json

df = pd.read_parquet("data/task_c/task_c_trial.parquet")

with open("data/task_c/id_to_label.json", "r") as file:
    id_to_label = json.load(file)

print("Official label mapping:")
print(id_to_label)

print("\nGenerator and label relationship:\n")

result = pd.crosstab(
    df["generator"] == "Human",
    df["label"]
)

print(result)

print("\nHuman samples:")
print(df[df["generator"] == "Human"][["generator", "label"]].head())

print("\nNon-human samples:")
print(df[df["generator"] != "Human"][["generator", "label"]].head())

print("\nVerified mapping from trial data:")
print("0 -> machine")
print("1 -> human")
print("2 -> hybrid")
print("3 -> adversarial")