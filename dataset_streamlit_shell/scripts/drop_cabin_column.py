import datetime
import json

import pandas as pd

p = "dataset_streamlit_shell/workspace/working.csv"
d = pd.read_csv(p)

d = d.drop(columns=["艙房"])
d.to_csv(p, index=False)

log = {
    "created_at": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    "actor": "agent",
    "action": "drop_cabin_column",
    "columns": ["艙房"],
    "rows": int(len(d)),
    "note": "刪除艙房欄位，保留是否有艙房旗標作為替代資訊。",
}
with open("dataset_streamlit_shell/workspace/cleaning_log.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(log, ensure_ascii=False) + "\n")

print(d.shape)
print(d.columns.tolist())
