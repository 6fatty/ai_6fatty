import pandas as pd

df = pd.read_csv('dataset_streamlit_shell/workspace/working.csv', encoding='utf-8-sig')
print('columns:', df.columns.tolist())
print('shape:', df.shape)
print('age_na_total:', int(df['年齡'].isna().sum()))
ch = df[df['同行父母子女數'] > 0]
print('has_children_rows:', len(ch))
print('has_children_age_na:', int(ch['年齡'].isna().sum()))
print('has_children_age_mean:', ch['年齡'].mean())
print('overall_age_mean:', df['年齡'].mean())
