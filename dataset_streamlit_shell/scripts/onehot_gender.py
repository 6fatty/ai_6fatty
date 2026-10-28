import json
from datetime import datetime

import pandas as pd

path = "dataset_streamlit_shell/workspace/working.csv"
df = pd.read_csv(path)
before_rows, before_cols = df.shape

# 1) 先確認欄位型態與類別值
print("轉換前:", df.shape, list(df.columns))
print(df["性別"].value_counts(dropna=False).to_dict())

# 2) one-hot：把 性別 拆成 性別_female / 性別_male，並轉成 0/1 整數
dummies = pd.get_dummies(df["性別"], prefix="性別")
dummies = dummies.astype(int)
df = pd.concat([df.drop(columns=["性別"]), dummies], axis=1)

print("轉換後:", df.shape, list(df.columns))
print(dummies.head(3).to_string())

df.to_csv(path, index=False)

log = {
    "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    "actor": "agent",
    "action": "one_hot_encode_gender",
    "columns": ["性別_female", "性別_male"],
    "rows": int(before_rows),
    "note": "以 one-hot 將性別欄位轉為性別_female與性別_male兩個0/1整數欄，並移除原始性別欄。",
}
with open("dataset_streamlit_shell/workspace/cleaning_log.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(log, ensure_ascii=False) + "\n")
print("log ok")
