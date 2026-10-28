import json, datetime
import pandas as pd

path = "dataset_streamlit_shell/workspace/working.csv"
df = pd.read_csv(path)

raw = df["Embarked"]
norm = raw.astype(str).str.strip().str.lower()

mapping = {}
for v in norm.unique():
    if v in ("s", "southampton"):
        mapping[v] = "S"
    elif v in ("c", "cherbourg"):
        mapping[v] = "C"
    elif v == "q":
        mapping[v] = "Q"
    elif v in ("nan", "none", "missing", ""):
        mapping[v] = None

new = norm.map(mapping)
changed = int((new.fillna("<NA>") != raw.fillna("<NA>")).sum())
nulls = int(new.isna().sum())

df["Embarked"] = new
df.to_csv(path, index=False)

entry = {
    "created_at": datetime.datetime.now().replace(microsecond=0).isoformat(),
    "actor": "agent",
    "action": "normalize_embarked_values",
    "columns": ["Embarked"],
    "rows": changed,
    "note": "將 Embarked 統一為 S/C/Q（Southampton→S、Cherbourg→C），空值保留待補。",
}
with open("dataset_streamlit_shell/workspace/cleaning_log.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print("mapping:", mapping)
print("changed rows:", changed)
print("nulls:", nulls)
print(df["Embarked"].value_counts(dropna=False).to_string())