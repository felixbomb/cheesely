import pandas as pd
df = pd.read_csv('/Users/felixbaum/projects/name_gen/cheese_data/archive/cheeses.csv')
print(df.head())

#step 1: normalize cheese attributes
df['cheese'] = df['cheese'].str.lower()
df['cheese'] = df['cheese'].str.replace(' ', '_', regex=False)
df['cheese'] = df['cheese'].str.replace('’', '_', regex=False)
df['cheese'] = df['cheese'].str.replace('\'', '_', regex=False)


df['milk'] = df['milk'].fillna('mystery animal')
df['type'] = df['type'].fillna('mystery type')
df['texture'] = df['texture'].fillna('mystery texture')
df_normalized = df[['cheese', 'milk', 'type', 'texture', 'url']]
df_normalized.set_index('cheese')

print(df_normalized.head())
df_normalized.to_csv('cheese_set.csv', index=False)