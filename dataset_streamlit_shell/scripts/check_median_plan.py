import pandas as pd

w = pd.read_csv('dataset_streamlit_shell/workspace/working.csv', encoding='utf-8-sig')
o = pd.read_csv('dataset_streamlit_shell/workspace/original.csv', encoding='utf-8-sig')

print('working', w.shape, 'original', o.shape)
print('working age_na', int(w['年齡'].isna().sum()), 'original age_na', int(o['年齡'].isna().sum()))
print('same index/cols:', list(w.columns) == list(o.columns))

ok = o['同行父母子女數'] > 0
print('original has_kids rows', int(ok.sum()))
print('original has_kids age_na', int((ok & o['年齡'].isna()).sum()))
print('original has_kids age mean', round(float(o.loc[ok, '年齡'].mean()), 4))
print('original has_kids age median', round(float(o.loc[ok, '年齡'].median()), 4))
print('original overall median', round(float(o['年齡'].median()), 4))

# 兩份檔案在其他欄位是否一致（確認 working 除了年齡以外沒被動過）
diff_cols = [c for c in w.columns if not w[c].equals(o[c])]
print('differing columns:', diff_cols)

# 確認 working 中那 20 筆是否確實等於 23.01
mask = ok & o['年齡'].isna()
print('working values at those rows:', sorted(set(w.loc[mask, '年齡'].round(2).tolist())))
