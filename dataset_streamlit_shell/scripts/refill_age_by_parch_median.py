import json
from datetime import datetime

import pandas as pd

path = 'dataset_streamlit_shell/workspace/working.csv'
df = pd.read_csv(path, encoding='utf-8-sig')

kids = df['同行父母子女數'] > 0
# 1) 還原上一次平均數補值的 20 筆（唯一指紋：23.01）
fp = kids & (df['年齡'].round(2) == 23.01)
restored = int(fp.sum())
df.loc[fp, '年齡'] = pd.NA

# 2) 以「有子女乘客」的中位數補值
median_age = float(df.loc[kids, '年齡'].median())
to_fill = kids & df['年齡'].isna()
n = int(to_fill.sum())
df.loc[to_fill, '年齡'] = round(median_age, 2)

df['年齡'] = df['年齡'].astype('float64')
df.to_csv(path, index=False, encoding='utf-8-sig')

rec = {
    "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    "actor": "agent",
    "action": "refill_missing_age_by_parch_median",
    "columns": ["年齡"],
    "rows": n,
    "note": f"先還原前次平均數補值的 {restored} 筆年齡，改以同行父母子女數大於 0 之乘客年齡中位數（{median_age:.2f}）補齊 {n} 筆空值。",
}
with open('dataset_streamlit_shell/workspace/cleaning_log.jsonl', 'a', encoding='utf-8') as f:
    f.write(json.dumps(rec, ensure_ascii=False) + "\n")

chk = pd.read_csv(path, encoding='utf-8-sig')
k = chk['同行父母子女數'] > 0
print('restored_to_na:', restored, 'filled:', n, 'median:', median_age)
print('remaining_age_na:', int(chk['年齡'].isna().sum()))
print('kids_age_na:', int(chk.loc[k, '年齡'].isna().sum()))
print('23.01 count now:', int((chk['年齡'].round(2) == 23.01).sum()), '22.0 count:', int((chk['年齡'].round(2) == 22.0).sum()))
print('shape:', chk.shape)
print('dtype:', chk['年齡'].dtype)
