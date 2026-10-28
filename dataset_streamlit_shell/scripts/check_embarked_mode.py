import pandas as pd

path = 'dataset_streamlit_shell/workspace/working.csv'
df = pd.read_csv(path, encoding='utf-8-sig')

s = df['登船港口']
print('dtype:', s.dtype)
print('na_count:', int(s.isna().sum()))
print('--- value_counts (dropna=False) ---')
print(s.value_counts(dropna=False).to_string())
print('--- raw repr of unique ---')
print([repr(v) for v in s.unique()])
print('mode:', s.mode().tolist())
print('blank-ish count:', int((s.astype(str).str.strip() == '').sum()))
