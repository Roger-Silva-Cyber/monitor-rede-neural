import pandas as pd

normal_path = '../dataset/trafego_normal.csv'
anormal_path = '../dataset/trafego_anormal.csv'

df_normal = pd.read_csv(normal_path)
df_anormal = pd.read_csv(anormal_path)

df_normal['label'] = 'normal'
df_anormal['label'] = 'anomalous'

df = pd.concat([df_normal, df_anormal], ignore_index=True)

df = df.sample(frac=1).reset_index(drop=True)

df.to_csv('../dataset/dados_final.csv', index=False)

print('[✔] Dataset combinado salvo como dados_final.csv')
