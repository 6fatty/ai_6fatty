import datetime
import json

import pandas as pd

p = "dataset_streamlit_shell/workspace/working.csv"
d = pd.read_csv(p)

d["是否有艙房"] = d["艙房"].notna().astype(int)
d.to_csv(p, index=False)

log = {
    "created_at": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    "actor": "agent",
    "action": "add_has_cabin_flag",
    "columns": ["是否有艙房"],
    "rows": int(len(d)),
    "note": "依艙房欄位是否有值新增是否有艙房旗標欄位（1=有、0=無）。",
}
with open("dataset_streamlit_shell/workspace/cleaning_log.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(log, ensure_ascii=False) + "\n")

print(d.shape)
print(d.columns.tolist())
print(d["是否有艙房"].value_counts().to_dict())
