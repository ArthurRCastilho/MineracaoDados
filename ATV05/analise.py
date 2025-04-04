import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import ta  # technical analysis library

# Baixando os dados dos últimos 12 meses
tickers = ['PETR4.SA', 'VALE3.SA']
dados = yf.download(tickers, period="12mo")['Close']
dados.dropna(inplace=True)

# Calculando indicadores técnicos
df = pd.DataFrame()
df['PETR4'] = dados['PETR4.SA']
df['VALE3'] = dados['VALE3.SA']

# PETR4 - Indicadores
df['PETR4_SMA20'] = df['PETR4'].rolling(window=20).mean()
df['PETR4_RSI'] = ta.momentum.RSIIndicator(df['PETR4']).rsi()
macd_petr4 = ta.trend.MACD(df['PETR4'])
df['PETR4_MACD'] = macd_petr4.macd_diff()

# VALE3 - Indicadores
df['VALE3_SMA20'] = df['VALE3'].rolling(window=20).mean()
df['VALE3_RSI'] = ta.momentum.RSIIndicator(df['VALE3']).rsi()
macd_vale3 = ta.trend.MACD(df['VALE3'])
df['VALE3_MACD'] = macd_vale3.macd_diff()

# Análise de retorno
retorno_petr4 = (df['PETR4'].iloc[-1] - df['PETR4'].iloc[0]) / df['PETR4'].iloc[0]
retorno_vale3 = (df['VALE3'].iloc[-1] - df['VALE3'].iloc[0]) / df['VALE3'].iloc[0]

print("Retorno PETR4 (últimos 12 meses): {:.2f}%".format(retorno_petr4 * 100))
print("Retorno VALE3 (últimos 12 meses): {:.2f}%".format(retorno_vale3 * 100))

# Plotando os preços e SMAs
df[['PETR4', 'PETR4_SMA20']].plot(title='PETR4 - Preço e SMA20', figsize=(10, 4))
plt.show()

df[['VALE3', 'VALE3_SMA20']].plot(title='VALE3 - Preço e SMA20', figsize=(10, 4))
plt.show()

# RSI e MACD (PETR4)
df[['PETR4_RSI']].plot(title='PETR4 - RSI', figsize=(10, 2), ylim=(0, 100))
plt.axhline(70, color='r', linestyle='--')
plt.axhline(30, color='g', linestyle='--')
plt.show()

df[['PETR4_MACD']].plot(title='PETR4 - MACD Diferença', figsize=(10, 2))
plt.axhline(0, color='black', linestyle='--')
plt.show()

# RSI e MACD (VALE3)
df[['VALE3_RSI']].plot(title='VALE3 - RSI', figsize=(10, 2), ylim=(0, 100))
plt.axhline(70, color='r', linestyle='--')
plt.axhline(30, color='g', linestyle='--')
plt.show()

df[['VALE3_MACD']].plot(title='VALE3 - MACD Diferença', figsize=(10, 2))
plt.axhline(0, color='black', linestyle='--')
plt.show()
