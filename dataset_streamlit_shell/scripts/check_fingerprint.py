import pandas as pd

path = 'dataset_streamlit_shell/workspace/working.csv'
w = pd.read_csv(path, encoding='utf-8-sig')

cand = (w['同行父母子女數'] > 0) & (w['年齡'].round(2) == 23.01)
print('rows matching 23.01 with kids:', int(cand.sum()))
print('exact 23.01 anywhere:', int((w['年齡'].round(2) == 23.01).sum()))

kids = w['同行父母子女數'] > 0
s = w.loc[kids, '年齡']
print('kids count', int(kids.sum()))
print('kids median (with filled)', round(float(s.median()), 4))
print('kids median (excluding fingerprint rows)', round(float(s[~cand[kids]].median()), 4))
print('min/max of kids age', s.min(), s.max())
