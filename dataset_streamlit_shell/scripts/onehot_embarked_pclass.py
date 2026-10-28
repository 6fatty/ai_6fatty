import json
from datetime import datetime

import pandas as pd

PATH = "dataset_streamlit_shell/workspace/working.csv"
TARGETS = ["登船港口", "艙等"]

df = pd.read_csv(PATH)
before_cols = list(df.columns)
print("轉換前:", df.shape, before_cols)

# 先確認類別值，避免出現意外的類別被靜默編碼
for c in TARGETS:
    print(c, df[c].value_counts(dropna=False).to_dict())

new_frames = []
for c in TARGETS:
    d = pd.get_dummies(df[c].astype(str), prefix=c).astype(int)
    d = d.reindex(columns=sorted(d.columns))  # 欄位排序，方便檢視
    new_frames.append(d)
    print(f"{c} ->", list(d.columns))

# 移除原欄位，原地插入 one-hot 欄（放在原欄位的位置，保持欄位順序乾淨）
cols = [c for c in before_cols if c not in TARGETS]
df_out = df.drop(columns=TARGETS)
insert_at = min(before_cols.index(c) for c in TARGETS)
blocks = pd.concat(new_frames, axis=1)
left = df_out.iloc[:, :insert_at]
right = df_out.iloc[:, insert_at:]
final = pd.concat([left, blocks, right], axis=1)

# 檢查：每組 one-hot 每列總和必須為 1
for c in TARGETS:
    grp = [col for col in final.columns if col.startswith(c + "_")]
    assert (final[grp].sum(axis=1) == 1).all(), f"{c} one-hot 不完整"
    print(f"{c} 欄位:", grp, "每列總和皆為 1 ✔")

final.to_csv(PATH, index=False)
print("轉換後:", final.shape, list(final.columns))
print(final.head(3).to_string())

added = [c for c in final.columns if c not in before_cols]
log = {
    "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    "actor": "agent",
    "action": "one_hot_encode_embarked_and_pclass",
    "columns": added,
    "rows": int(len(final)),
    "note": "以 one-hot 將登船港口拆為S/C/Q三欄、艙等拆為1/2/3三欄，皆為0/1整數並移除原始兩欄。",
}
with open("dataset_streamlit_shell/workspace/cleaning_log.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(log, ensure_ascii=False) + "\n")
print("log ok")
