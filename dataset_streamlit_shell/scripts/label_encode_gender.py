import json
from datetime import datetime

import pandas as pd

path = "dataset_streamlit_shell/workspace/working.csv"
df = pd.read_csv(path)

print("轉換前:", df.shape, list(df.columns))

# 用現有 one-hot 欄位反推原始性別，不需動用 original.csv
assert ((df["性別_female"] + df["性別_male"]) == 1).all(), "one-hot 欄位不互補，需人工檢查"

# 單欄 label encoding：female = 1, male = 0
df["性別"] = df["性別_female"].astype(int)
df = df.drop(columns=["性別_female", "性別_male"])

# 把 性別 放回原本的位置（第 5 欄，即 姓名 之後）
cols = list(df.columns)
cols.remove("性別")
cols.insert(cols.index("姓名") + 1, "性別")
df = df[cols]

df["性別"] = df["性別"].astype(int)
df.to_csv(path, index=False)

print("轉換後:", df.shape, list(df.columns))
print(df["性別"].value_counts().to_dict())
print("dtype:", df["性別"].dtype)

log = {
    "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    "actor": "agent",
    "action": "label_encode_gender",
    "columns": ["性別"],
    "rows": int(len(df)),
    "note": "將性別合併為單一整數欄並移除性別_female、性別_male兩欄，female記為1、male記為0。",
}
with open("dataset_streamlit_shell/workspace/cleaning_log.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(log, ensure_ascii=False) + "\n")
print("log ok")
