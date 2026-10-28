import pandas as pd
df = pd.read_csv("dataset_streamlit_shell/workspace/working.csv")
dup = df[df.duplicated(subset=["Name"], keep=False)].sort_values("Name")
print("rows:", len(df))
print("dup rows involved:", len(dup))
print("extra rows to drop:", df.duplicated(subset=["Name"]).sum())
print(dup[["PassengerId","Name","Sex","Age","Fare","Embarked"]].to_string())
