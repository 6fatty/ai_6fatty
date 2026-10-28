import pandas as pd

path = 'dataset_streamlit_shell/workspace/working.csv'
df = pd.read_csv(path, encoding='utf-8-sig')

age = df['年齡']
print('total na:', int(age.isna().sum()))
kids = df['同行父母子女數'] > 0
print('kids rows:', int(kids.sum()), 'kids na:', int((kids & age.isna()).sum()))
print('no-kids rows:', int((~kids).sum()), 'no-kids na:', int((~kids & age.isna()).sum()))
print('dtype:', age.dtype)
print('describe:')
print(age.describe().to_string())
print('--- na by 性別 ---')
print(df.loc[age.isna(), '性別'].value_counts(dropna=False).to_string())
print('--- na by 艙等 ---')
print(df.loc[age.isna(), '艙等'].value_counts(dropna=False).to_string())
print('--- na by 同行兄弟姊妹配偶數 ---')
print(df.loc[age.isna(), '同行兄弟姊妹配偶數'].value_counts(dropna=False).to_string())
print('sex median/mean:')
print(df.groupby('性別')['年齡'].agg(['count', 'mean', 'median']).round(2).to_string())
