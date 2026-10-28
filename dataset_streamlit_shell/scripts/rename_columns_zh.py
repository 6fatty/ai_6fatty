import json, datetime
import pandas as pd

path = "dataset_streamlit_shell/workspace/working.csv"
df = pd.read_csv(path)

mapping = {
    "PassengerId": "乘客編號",
    "Survived": "是否生還",
    "Pclass": "艙等",
    "Name": "姓名",
    "Sex": "性別",
    "Age": "年齡",
    "SibSp": "同行兄弟姊妹配偶數",
    "Parch": "同行父母子女數",
    "Ticket": "票號",
    "Fare": "票價",
    "Cabin": "艙房",
    "Embarked": "登船港口",
}
df = df.rename(columns=mapping)
df.to_csv(path, index=False)

entry = {
    "created_at": datetime.datetime.now().replace(microsecond=0).isoformat(),
    "actor": "agent",
    "action": "rename_columns_to_zh",
    "columns": list(mapping.keys()),
    "rows": 891,
    "note": "將 12 個欄位名稱由英文改為繁體中文。",
}
with open("dataset_streamlit_shell/workspace/cleaning_log.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(list(df.columns))