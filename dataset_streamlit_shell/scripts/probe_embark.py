import pandas as pd

df = pd.read_csv("dataset_streamlit_shell/workspace/working.csv")
out = [str(df.shape), str(list(df.columns))]
for c in ["登船港口", "艙等"]:
    out.append(f"--- {c} dtype={df[c].dtype} NaN={int(df[c].isna().sum())}")
    out.append(df[c].value_counts(dropna=False).to_string())
with open("dataset_streamlit_shell/scripts/probe_embark_out.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
