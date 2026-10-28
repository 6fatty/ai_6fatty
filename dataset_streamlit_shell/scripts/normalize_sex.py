import json, datetime
import pandas as pd

path = "dataset_streamlit_shell/workspace/working.csv"
df = pd.read_csv(path)

male_set = {"m", "male", "man", "men", "masculine"}
female_set = {"f", "female", "woman", "women", "fem", "feminine"}

raw = df["Sex"]
norm = raw.astype(str).str.strip().str.lower()

mapping = {}
for v in norm.unique():
    if v in male_set:
        mapping[v] = "male"
    elif v in female_set:
        mapping[v] = "female"

new = norm.map(mapping)
changed = int((new != raw).sum())

df["Sex"] = new
df.to_csv(path, index=False)

entry = {
    "created_at": datetime.datetime.now().replace(microsecond=0).isoformat(),
    "actor": "agent",
    "action": "normalize_sex_values",
    "columns": ["Sex"],
    "rows": changed,
    "note": "將 Sex 欄位的男性變體統一為 male、女性變體統一為 female。",
}
with open("dataset_streamlit_shell/workspace/cleaning_log.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print("mapping:", mapping)
print("changed rows:", changed)
print(df["Sex"].value_counts(dropna=False).to_string())
