import json
from datetime import datetime

import pandas as pd

path = 'dataset_streamlit_shell/workspace/working.csv'
df = pd.read_csv(path, encoding='utf-8-sig')

col = '登船港口'
mode_val = df[col].mode(dropna=True).iloc[0]
mask = df[col].isna()
n = int(mask.sum())
df.loc[mask, col] = mode_val

df.to_csv(path, index=False, encoding='utf-8-sig')

rec = {
    "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    "actor": "agent",
    "action": "fill_missing_embarked_mode",
    "columns": [col],
    "rows": n,
    "note": f"以登船港口的眾數（{mode_val}）補齊空值共 {n} 筆。",
}
with open('dataset_streamlit_shell/workspace/cleaning_log.jsonl', 'a', encoding='utf-8') as f:
    f.write(json.dumps(rec, ensure_ascii=False) + "\n")

chk = pd.read_csv(path, encoding='utf-8-sig')
print('filled:', n, 'with:', mode_val)
print('remaining na:', int(chk[col].isna().sum()))
print(chk[col].value_counts(dropna=False).to_string())
print('shape:', chk.shape)
