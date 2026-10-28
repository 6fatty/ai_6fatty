import pandas as pd

path = 'dataset_streamlit_shell/workspace/working.csv'
df = pd.read_csv(path, encoding='utf-8-sig')

for c in ['票號', '票價']:
    s = df[c]
    print('=' * 50)
    print('column:', c, 'dtype:', s.dtype)
    print('na:', int(s.isna().sum()), 'unique:', int(s.nunique()))
    vc = s.value_counts(dropna=True)
    print('top5:')
    print(vc.head(5).to_string())
    m = s.mode()
    print('mode list(前3):', m.head(3).tolist(), 'mode_count:', len(m))
    if len(m) > 0:
        print('mode frequency:', int(vc.iloc[0]), 'coverage:', round(vc.iloc[0] / s.notna().sum() * 100, 2), '%')
    print('raw unique sample:', [repr(v) for v in s.dropna().unique()[:6]])

print('=' * 50)
print('票價 describe:')
print(df['票價'].describe().to_string())
print('票價 median:', df['票價'].median())
print('missing rows both/one:')
print('票號 na & 票價 na:', int((df['票號'].isna() & df['票價'].isna()).sum()))
