import pandas as pd

# Ler o arquivo CSV original
df = pd.read_csv("/Users/arthurlavidali/Python/ATV02/ds_salaries.csv")

# Salvar com as especificações desejadas
df.to_csv("ds_trans_salario.csv", sep=';', decimal=',', encoding='utf-8', index=False)
