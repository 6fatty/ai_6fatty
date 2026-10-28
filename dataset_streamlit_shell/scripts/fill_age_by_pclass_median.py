import json
from datetime import datetime

import pandas as pd

path = 'dataset_streamlit_shell/workspace/working.csv'
df = pd.read_csv(path, encoding='utf-8-sig')

col = '年齡'
med = df.groupby('艙等')[col].median()
mask = df[col].isna()
n = int(mask.sum())

df.loc[mask, col] = df.loc[mask, '艙等'].map(med)

df[col] = df[col].astype('float64')
df.to_csv(path, index=False, encoding='utf-8-sig')

detail = "、".join(f"{int(k)}等 {v:g}" for k, v in med.items())
rec = {
    "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    "actor": "agent",
    "action": "fill_missing_age_by_pclass_median",
    "columns": [col, "艙等"],
    "rows": n,
    "note": f"以各艙等年齡中位數（{detail}）補齊年齡空值共 {n} 筆。",
}
with open('dataset_streamlit_shell/workspace/cleaning_log.jsonl', 'a', encoding='utf-8') as f:
    f.write(json.dumps(rec, ensure_ascii=False) + "\n")

chk = pd.read_csv(path, encoding='utf-8-sig')
print('filled:', n)
print('remaining na:', int(chk[col].isna().sum()))
print('shape:', chk.shape)
print(chk.groupby('艙等')[col].agg(['count', 'median', 'mean', 'min', 'max']).round(2).to_string())
print('overall median:', chk[col].median(), 'mean:', round(chk[col].mean(), 2))
