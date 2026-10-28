import pandas as pd

df = pd.read_csv("dataset_streamlit_shell/workspace/working.csv")
out = []
out.append(str(df.shape))
out.append(str(list(df.columns)))
out.append(str(df["性別"].dtype))
out.append(df["性別"].value_counts().sort_index().to_string())
out.append(df.head(3).to_string())
out.append("NaN in 性別: " + str(int(df["性別"].isna().sum())))
with open("dataset_streamlit_shell/scripts/verify_out.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
