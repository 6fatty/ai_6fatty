import json, datetime
import pandas as pd

path = "dataset_streamlit_shell/workspace/working.csv"
df = pd.read_csv(path)
before = len(df)

# 以 Name 為鍵去重：同一個 Name 保留「非空值最多」的那一列，若相同則保留先出現的
df["_nonnull"] = df.notna().sum(axis=1)
df["_order"] = range(len(df))
df = (df.sort_values(["_nonnull", "_order"], ascending=[False, True])
        .drop_duplicates(subset=["Name"], keep="first")
        .sort_values("_order")
        .drop(columns=["_nonnull", "_order"])
        .reset_index(drop=True))

after = len(df)
dropped = before - after
df.to_csv(path, index=False)

entry = {
    "created_at": datetime.datetime.now().replace(microsecond=0).isoformat(),
    "actor": "agent",
    "action": "drop_duplicate_name",
    "columns": ["Name"],
    "rows": dropped,
    "note": "以 Name 為鍵去重，同名者保留資料較完整的一列，共刪除 2 筆重複。",
}
with open("dataset_streamlit_shell/workspace/cleaning_log.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print("before:", before, "after:", after, "dropped:", dropped)
print("remaining dup names:", df.duplicated(subset=["Name"]).sum())
