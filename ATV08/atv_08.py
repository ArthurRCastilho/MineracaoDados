import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 01
# Carregar a base
df = pd.read_csv('california_housing_train.csv')

# Colunas de interesse
cols = ['median_income', 'median_house_value', 'housing_median_age']

# Estatísticas básicas
stats_df = df[cols].agg(['mean', 'median', 'std', 'min', 'max', pd.Series.mode]).T
stats_df.columns = ['Média', 'Mediana', 'Desvio Padrão', 'Mínimo', 'Máximo', 'Moda']

# Quartis e IQR
quartis = df[cols].quantile([0.25, 0.5, 0.75])
iqr = quartis.loc[0.75] - quartis.loc[0.25]

# Detecção de outliers (regra do IQR)
outliers = {}
for col in cols:
    q1 = quartis.loc[0.25, col]
    q3 = quartis.loc[0.75, col]
    iqr_value = q3 - q1
    lower_bound = q1 - 1.5 * iqr_value
    upper_bound = q3 + 1.5 * iqr_value
    outliers[col] = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()

print("Estatísticas:")
print(stats_df)
print("\nOutliers detectados:")
print(outliers)

# ------------------------
# 02
# Carregar base
df2 = pd.read_csv('Economy_of_US_na.csv')

# Identificar colunas com valores ausentes
missing_cols = df2.columns[df2.isnull().any()]
print("Colunas com valores ausentes:", missing_cols.tolist())

# Estratégia 1: Preencher com a média
df_filled_mean = df2.copy()
df_filled_mean[missing_cols] = df_filled_mean[missing_cols].fillna(df_filled_mean.mean(numeric_only=True))

# Estratégia 2: Remover linhas com muitos valores ausentes (menos de 3 colunas não nulas)
df_dropped = df2.dropna(thresh=3)

print("Dados preenchidos com a média (amostra):")
print(df_filled_mean.head())
print("\nDados com linhas removidas:")
print(df_dropped.head())


# ------------------------
# 03
# Carregar base
df3 = pd.read_csv('Nov2Temp.csv')

# Amostragem de 15% sem reposição
sample1 = df3.sample(frac=0.15, replace=False, random_state=42)

# Amostragem de 20% com reposição
sample2 = df3.sample(frac=0.20, replace=True, random_state=42)

print(f"Amostra 15% sem reposição: {sample1.shape[0]} linhas")
print(f"Amostra 20% com reposição: {sample2.shape[0]} linhas")

# Explicação:
print("""
Diferença prática:
- Amostragem **sem reposição**: cada elemento pode ser escolhido apenas uma vez. É ideal para garantir diversidade e evitar duplicações.
- Amostragem **com reposição**: um mesmo dado pode ser escolhido várias vezes. Usada em simulações e bootstrap.
""")

# ------------------------
# 04
# Quartis da renda
quartis_income = df['median_income'].quantile([0.25, 0.5, 0.75])

# Criar categorias com base nos quartis
bins = [df['median_income'].min() - 1, quartis_income[0.25], quartis_income[0.5], quartis_income[0.75], df['median_income'].max()]
labels = ['Baixa renda', 'Média-baixa', 'Média-alta', 'Alta renda']
df['faixa_renda'] = pd.cut(df['median_income'], bins=bins, labels=labels)

# Gráfico de barras
df['faixa_renda'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Distribuição por Faixa de Renda')
plt.xlabel('Faixa de Renda')
plt.ylabel('Número de Casas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


