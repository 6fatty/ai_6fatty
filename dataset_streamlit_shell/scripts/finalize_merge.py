import json, datetime, os
from pathlib import Path

base = Path("dataset_streamlit_shell/workspace")
entry = {
    "created_at": datetime.datetime.now().replace(microsecond=0).isoformat(),
    "actor": "agent",
    "action": "merge_dual_table",
    "columns": ["PassengerId", "Ticket", "Fare", "Cabin", "Embarked"],
    "rows": 893,
    "note": "以 PassengerId 為鍵 left 合併乘客表與航程表，寫入 Original 與 Working。",
}
with open(base / "cleaning_log.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(entry, ensure_ascii=False) + "\n")

for name in ["passengers.csv", "voyage.csv"]:
    (base / "integration" / name).unlink()
(base / "integration").rmdir()
print("log ok; remaining:", sorted(os.listdir(base)))
