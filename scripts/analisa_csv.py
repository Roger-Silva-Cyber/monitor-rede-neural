import pandas as pd

# Caminho do CSV
df = pd.read_csv('../dataset/dados_final.csv')

# Exibir as 5 primeiras linhas
print('\n📌 Primeiras linhas do dataset:')
print(df.head())

# Contar quantos pacotes são normais vs anômalos
print('\n📊 Contagem de rótulos:')
print(df['label'].value_counts())

# Verificar se há valores ausentes
print('\n🧪 Verificação de valores ausentes:')
print(df.isnull().sum())

# Estatísticas descritivas
print('\n📈 Estatísticas descritivas:')
print(df.describe())
