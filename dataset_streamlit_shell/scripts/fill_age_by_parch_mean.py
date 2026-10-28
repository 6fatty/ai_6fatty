import json
from datetime import datetime

import pandas as pd

path = 'dataset_streamlit_shell/workspace/working.csv'
df = pd.read_csv(path, encoding='utf-8-sig')

has_kids = df['同行父母子女數'] > 0
mean_age = df.loc[has_kids, '年齡'].mean()

mask = has_kids & df['年齡'].isna()
n = int(mask.sum())
df.loc[mask, '年齡'] = round(float(mean_age), 2)

df.to_csv(path, index=False, encoding='utf-8-sig')

rec = {
    "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    "actor": "agent",
    "action": "fill_missing_age_by_parch_mean",
    "columns": ["年齡"],
    "rows": n,
    "note": f"以同行父母子女數大於 0 之乘客的年齡平均（{mean_age:.2f}）補齊其年齡空值 {n} 筆。",
}
with open('dataset_streamlit_shell/workspace/cleaning_log.jsonl', 'a', encoding='utf-8') as f:
    f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print('filled:', n, 'mean:', round(float(mean_age), 2))
chk = pd.read_csv(path, encoding='utf-8-sig')
print('remaining_age_na:', int(chk['年齡'].isna().sum()))
print('shape:', chk.shape)
print(chk.loc[chk['同行父母子女數'] > 0, '年齡'].dropna().iloc[:5].tolist())
