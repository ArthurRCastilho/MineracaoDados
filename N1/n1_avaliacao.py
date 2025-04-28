import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 1. Coleta de Dados com Web Scraping (API yfinance)
print("1. Coletando dados históricos de VALE3 e PETR4...")

tickers = ['VALE3.SA', 'PETR4.SA']
dados = {}

for ticker in tickers:
    dados[ticker] = yf.download(ticker, start='2014-01-01', end='2024-01-01', interval='1mo')

# Salvando em CSV
for ticker in tickers:
    df = dados[ticker]['Close'].reset_index()
    df.columns = ['Data', 'Preco_Fechamento']
    df.to_csv(f'{ticker}_precos.csv', sep=';', index=False)

print("Dados coletados e salvos.")

# 2. Cálculo dos Retornos Mensais
print("\n2. Calculando retornos mensais...")

retornos = []

for ticker in tickers:
    df = pd.read_csv(f'{ticker}_precos.csv', sep=';', parse_dates=['Data'])
    df['Retorno'] = df['Preco_Fechamento'].pct_change() * 100
    df = df.dropna()
    df['Acao'] = ticker
    retornos.append(df[['Data', 'Acao', 'Retorno']])

retornos_df = pd.concat(retornos)
retornos_df.to_csv('retornos_mensais.csv', sep=';', index=False)

print("Retornos calculados e salvos.")

# 3. Estatística Descritiva
print("\n3. Calculando estatísticas descritivas...")

estatisticas = {}

for acao in retornos_df['Acao'].unique():
    temp = retornos_df[retornos_df['Acao'] == acao]['Retorno']
    estatisticas[acao] = {
        'media': temp.mean(),
        'mediana': temp.median(),
        'moda': temp.mode().iloc[0] if not temp.mode().empty else np.nan,
        'desvio_padrao': temp.std(),
        'Q1': temp.quantile(0.25),
        'Q2': temp.quantile(0.5),
        'Q3': temp.quantile(0.75),
        'minimo': temp.min(),
        'maximo': temp.max()
    }

estatisticas = pd.DataFrame(estatisticas).T
estatisticas['IQR'] = estatisticas['Q3'] - estatisticas['Q1']

print(estatisticas)

# 4. Detecção de Outliers
print("\n4. Detectando outliers usando o IQR...")

outliers = {}

for acao in retornos_df['Acao'].unique():
    temp = retornos_df[retornos_df['Acao'] == acao]
    Q1 = estatisticas.loc[acao, 'Q1']
    Q3 = estatisticas.loc[acao, 'Q3']
    IQR = estatisticas.loc[acao, 'IQR']
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    outlier_temp = temp[(temp['Retorno'] < limite_inferior) | (temp['Retorno'] > limite_superior)]
    outliers[acao] = outlier_temp

for acao, df_outliers in outliers.items():
    print(f"\nOutliers detectados para {acao}:")
    print(df_outliers[['Data', 'Retorno']])

# 5. Teste de Hipótese – t-teste
print("\n5. Realizando t-teste de independência entre retornos de VALE3 e PETR4...")

retorno_vale3 = retornos_df[retornos_df['Acao'] == 'VALE3.SA']['Retorno']
retorno_petr4 = retornos_df[retornos_df['Acao'] == 'PETR4.SA']['Retorno']

t_stat, p_valor = stats.ttest_ind(retorno_vale3, retorno_petr4, equal_var=False)

print(f"Valor de p: {p_valor:.5f}")

if p_valor < 0.05:
    print("Resultado: Existe diferença significativa entre os retornos médios.")
else:
    print("Resultado: Não existe diferença significativa entre os retornos médios.")

# 6. Visualizações
print("\n6. Gerando visualizações...")

# Boxplot comparativo
plt.figure(figsize=(10, 6))
sns.boxplot(x='Acao', y='Retorno', data=retornos_df)
plt.title('Boxplot de Retornos Mensais: VALE3 vs PETR4')
plt.grid()
plt.show()

# Histogramas
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
sns.histplot(retornos_df[retornos_df['Acao'] == 'VALE3.SA']['Retorno'], kde=True, bins=20, color='blue')
plt.title('Histograma de Retornos VALE3')
plt.grid()

plt.subplot(1, 2, 2)
sns.histplot(retornos_df[retornos_df['Acao'] == 'PETR4.SA']['Retorno'], kde=True, bins=20, color='green')
plt.title('Histograma de Retornos PETR4')
plt.grid()

plt.tight_layout()
plt.show()

# Gráfico de evolução acumulada dos retornos
retornos_df['Retorno_Acumulado'] = retornos_df.groupby('Acao')['Retorno'].cumsum()

plt.figure(figsize=(12, 6))
for acao in retornos_df['Acao'].unique():
    dados_plot = retornos_df[retornos_df['Acao'] == acao]
    plt.plot(dados_plot['Data'], dados_plot['Retorno_Acumulado'], label=acao)

plt.title('Evolução Acumulada dos Retornos')
plt.xlabel('Data')
plt.ylabel('Retorno Acumulado (%)')
plt.legend()
plt.grid()
plt.show()

# 7. Conclusão Analítica
print("\nConclusão Analítica:")

# 7.1 - Análise de Retorno Médio
media_vale3 = estatisticas.loc['VALE3.SA', 'media']
media_petr4 = estatisticas.loc['PETR4.SA', 'media']

print("\n- Retorno Médio:")
print(f"VALE3 teve um retorno médio de {media_vale3:.2f}% ao mês.")
print(f"PETR4 teve um retorno médio de {media_petr4:.2f}% ao mês.")

if media_vale3 > media_petr4:
    print("VALE3 apresentou um retorno médio superior a PETR4.")
else:
    print("PETR4 apresentou um retorno médio superior a VALE3.")

# 7.2 - Análise de Variabilidade (Risco)
desvio_vale3 = estatisticas.loc['VALE3.SA', 'desvio_padrao']
desvio_petr4 = estatisticas.loc['PETR4.SA', 'desvio_padrao']

print("\n- Risco (Variabilidade dos Retornos):")
print(f"Desvio padrão dos retornos de VALE3: {desvio_vale3:.2f}")
print(f"Desvio padrão dos retornos de PETR4: {desvio_petr4:.2f}")

if desvio_vale3 > desvio_petr4:
    print("VALE3 apresentou maior volatilidade (risco) em relação a PETR4.")
else:
    print("PETR4 apresentou maior volatilidade (risco) em relação a VALE3.")

# 7.3 - Perfil de Investidor Ideal
print("\n- Perfil de Investidor Ideal:")
if media_vale3 > media_petr4 and desvio_vale3 < desvio_petr4:
    print("VALE3 combina melhor retorno com menor risco, sendo mais atrativa para perfis moderados a agressivos.")
elif media_petr4 > media_vale3 and desvio_petr4 < desvio_vale3:
    print("PETR4 combina melhor retorno com menor risco, sendo mais atrativa para perfis moderados a agressivos.")
else:
    print("Ambas as ações apresentam características distintas. VALE3 ou PETR4 podem ser escolhidas conforme o apetite ao risco do investidor.")

# 7.4 - Resultado do Teste de Hipótese
print("\n- Teste de Hipótese (Comparação de Retornos Médios):")
if p_valor < 0.05:
    print("O teste de hipótese indicou que existe uma diferença estatisticamente significativa entre os retornos médios de VALE3 e PETR4.")
else:
    print("O teste de hipótese indicou que não existe diferença estatisticamente significativa entre os retornos médios de VALE3 e PETR4.")

print("\nAnálise concluída.")
