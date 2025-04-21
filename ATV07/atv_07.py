import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# === Parte 1 – Estatística Descritiva ===

# Carregar dados com separador ';'
df = pd.read_csv('seuarquivo.csv', sep=';')

# Estatísticas para salário e nota_avaliacao
for col in ['salario', 'nota_avaliacao']:
    print(f"\nAnálise para: {col}")
    print(f"Média: {df[col].mean()}")
    print(f"Mediana: {df[col].median()}")
    print(f"Moda: {df[col].mode()[0]}")
    print(f"Desvio Padrão: {df[col].std()}")
    print(f"Mínimo: {df[col].min()}")
    print(f"Máximo: {df[col].max()}")
    print(f"Q1: {df[col].quantile(0.25)}")
    print(f"Q2 (Mediana): {df[col].quantile(0.50)}")
    print(f"Q3: {df[col].quantile(0.75)}")
    print(f"IQR: {df[col].quantile(0.75) - df[col].quantile(0.25)}")

# Boxplots
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(data=df, y='salario')
plt.title('Boxplot - Salário')

plt.subplot(1, 2, 2)
sns.boxplot(data=df, y='nota_avaliacao')
plt.title('Boxplot - Nota de Avaliação')
plt.tight_layout()
plt.show()

# Histograma de idade
plt.figure(figsize=(6, 4))
plt.hist(df['idade'], bins=10, edgecolor='black')
plt.title('Histograma - Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()

# === Parte 2 – Detecção de Outliers ===

# Cálculo do IQR
Q1 = df['salario'].quantile(0.25)
Q3 = df['salario'].quantile(0.75)
IQR = Q3 - Q1

# Limites
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Filtrando outliers
outliers = df[(df['salario'] < limite_inferior) | (df['salario'] > limite_superior)]

print("\nPessoas com salário fora do intervalo (outliers):")
print(outliers[['nome', 'salario']])

# === Parte 3 – Teste de Hipótese ===

grupo_brasil = df[df['pais'] == 'Brasil']['salario']
grupo_eua = df[df['pais'] == 'EUA']['salario']

# Teste t (variância diferente: equal_var=False)
t_stat, p_val = stats.ttest_ind(grupo_brasil, grupo_eua, equal_var=False)

print(f"\nT-Statistic: {t_stat}")
print(f"P-Value: {p_val}")

if p_val < 0.05:
    print("Rejeitamos H₀: Há diferença significativa entre os salários.")
else:
    print("Não rejeitamos H₀: Não há diferença significativa entre os salários.")

# === Parte 4 – Conclusão Reflexiva ===

"""
1. Há desigualdade salarial entre os países?
→ (Responda com base no p-valor: se < 0.05, há diferença significativa)

2. Como os conceitos estatísticos ajudaram a compreender os dados?
→ Permitem observar distribuição, valores extremos (outliers), comparar grupos e validar hipóteses com testes estatísticos.

3. Qual variável apresenta maior dispersão?
→ Compare os desvios padrão de 'salario' e 'nota_avaliacao' para identificar.
"""
