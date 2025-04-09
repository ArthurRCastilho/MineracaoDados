# Arthur Rodrigues Castilho

import pandas as pd

# 1
df = pd.read_csv('california_housing_test.csv')
df.head()


# 2
df_1 = df[['longitude', 'latitude', 'median_income']].iloc[0:10]
df_2 = df[['longitude', 'latitude', 'median_income']].iloc[10:20]
df_3 = df[['longitude', 'latitude', 'median_income']].iloc[20:30]

# 3
df_vertical = pd.concat([df_1, df_2, df_3], axis=0)
print(df_vertical)

# 4
df_horizontal = pd.concat([df_1, df_2, df_3], axis=1)
print(df_horizontal)

# 5
df_1['company_location'] = ['A'] * 10
df_2['company_location'] = ['A'] * 5 + ['B'] * 5

# 6
merge_inner = pd.merge(df_1, df_2, on='company_location', how='inner')
print(merge_inner)

# 7 
merge_left = pd.merge(df_1, df_2, on='company_location', how='left')
merge_right = pd.merge(df_1, df_2, on='company_location', how='right')
merge_outer = pd.merge(df_1, df_2, on='company_location', how='outer')
