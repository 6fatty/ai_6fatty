import pandas as pd

path = 'dataset_streamlit_shell/workspace/working.csv'
df = pd.read_csv(path, encoding='utf-8-sig')

g = df.groupby('艙等')['年齡'].agg(['count', 'median', 'mean']).round(2)
print(g.to_string())
na = df['年齡'].isna()
print('--- na count by 艙等 ---')
print(df.loc[na, '艙等'].value_counts().sort_index().to_string())
print('na total:', int(na.sum()))
