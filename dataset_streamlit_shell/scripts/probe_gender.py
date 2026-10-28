import pandas as pd

df = pd.read_csv("dataset_streamlit_shell/workspace/working.csv")
lines = [f"shape={df.shape}", f"cols={list(df.columns)}"]
lines.append("性別 value_counts:")
lines.append(df["性別"].value_counts(dropna=False).to_string())
lines.append(f"性別 NaN 筆數={int(df['性別'].isna().sum())}")
lines.append(f"dtype={df['性別'].dtype}")
with open("dataset_streamlit_shell/scripts/probe_gender_out.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
