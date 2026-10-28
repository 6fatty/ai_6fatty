import pandas as pd
df = pd.read_csv("dataset_streamlit_shell/workspace/working.csv")
print(df["Sex"].value_counts(dropna=False).to_string())
print("nulls:", df["Sex"].isna().sum())
