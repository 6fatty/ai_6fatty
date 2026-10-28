import json
from datetime import datetime

import pandas as pd

path = 'dataset_streamlit_shell/workspace/working.csv'
df = pd.read_csv(path, encoding='utf-8-sig')

# 票價：並列眾數取最小值 8.05
fare_mask = df['票價'].isna()
n_fare = int(fare_mask.sum())
fare_mode = float(df['票價'].mode().min())
df.loc[fare_mask, '票價'] = fare_mode

# 票號：填 UNKNOWN
tick_mask = df['票號'].isna()
n_tick = int(tick_mask.sum())
df.loc[tick_mask, '票號'] = 'UNKNOWN'

df.to_csv(path, index=False, encoding='utf-8-sig')

rec = {
    "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    "actor": "agent",
    "action": "fill_missing_fare_mode_ticket_unknown",
    "columns": ["票號", "票價"],
    "rows": max(n_fare, n_tick),
    "note": f"票價以並列眾數取最小值 {fare_mode} 補齊 {n_fare} 筆；票號為識別碼，空值 {n_tick} 筆以 UNKNOWN 標記，不使用眾數避免製造重複身份。",
}
with open('dataset_streamlit_shell/workspace/cleaning_log.jsonl', 'a', encoding='utf-8') as f:
    f.write(json.dumps(rec, ensure_ascii=False) + "\n")

chk = pd.read_csv(path, encoding='utf-8-sig')
print('filled fare:', n_fare, '->', fare_mode)
print('filled ticket:', n_tick, '-> UNKNOWN')
print('fare na:', int(chk['票價'].isna().sum()), '| ticket na:', int(chk['票號'].isna().sum()))
print('UNKNOWN count:', int((chk['票號'] == 'UNKNOWN').sum()))
print('shape:', chk.shape)
print('--- 全表缺失值總檢查 ---')
print(chk.isna().sum().to_string())
