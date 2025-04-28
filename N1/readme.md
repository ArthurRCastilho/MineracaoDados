# Avaliação 01 - N1

# Alunos
- [Arthur Rodrigues](https://github.com/ArthurRCastilho)
- [Rhennan Augusto Santana do Carmo](https://github.com/RhennanAugusto)

## Retorno
- [n1_avaliacao.py](https://github.com/ArthurRCastilho/MineracaoDados/blob/main/N1/n1_avaliacao.py) <br>

1. Coletando dados históricos de VALE3 e PETR4...<br>
YF.download() has changed argument auto_adjust default to True<br>
[*********************100%***********************]  1 of 1 completed<br>
[*********************100%***********************]  1 of 1 completed<br>
Dados coletados e salvos.<br>

2. Calculando retornos mensais...<br>
Retornos calculados e salvos.<br>

3. Calculando estatísticas descritivas...<br>
             media   mediana       moda  desvio_padrao        Q1        Q2        Q3     minimo     maximo        IQR<br>
VALE3.SA  1.863866  0.721682 -27.780597      11.424122 -6.559879  0.721682  7.726991 -27.780597  29.966988  14.286869<br>
PETR4.SA  2.702020  2.708787 -44.790834      14.359424 -5.638865  2.708787  9.567598 -44.790834  61.673077  15.206463<br>

4. Detectando outliers usando o IQR...<br>

Outliers detectados para VALE3.SA:<br>
         Data    Retorno<br>
27 2016-04-01  29.966988<br>

Outliers detectados para PETR4.SA:<br>
         Data    Retorno<br>
15 2015-04-01  35.196686<br>
26 2016-03-01  61.673077<br>
74 2020-03-01 -44.790834<br>

5. Realizando t-teste de independência entre retornos de VALE3 e PETR4...<br>
Valor de p: 0.61877<br>
Resultado: Não existe diferença significativa entre os retornos médios.<br>

6. Gerando visualizações...<br>

Conclusão Analítica:<br>

- Retorno Médio:<br>
VALE3 teve um retorno médio de 1.86% ao mês.<br>
PETR4 teve um retorno médio de 2.70% ao mês.<br>
PETR4 apresentou um retorno médio superior a VALE3.<br>

- Risco (Variabilidade dos Retornos):<br>
Desvio padrão dos retornos de VALE3: 11.42<br>
Desvio padrão dos retornos de PETR4: 14.36<br>
PETR4 apresentou maior volatilidade (risco) em relação a VALE3.<br>

- Perfil de Investidor Ideal:<br>
Ambas as ações apresentam características distintas. VALE3 ou PETR4 podem ser escolhidas conforme o apetite ao risco do investidor.<br>

- Teste de Hipótese (Comparação de Retornos Médios):<br>
O teste de hipótese indicou que não existe diferença estatisticamente significativa entre os retornos médios de VALE3 e PETR4.<br>

Análise concluída.<br>

## Gráficos
<img src="./imgs/Graf01.jpg" alt="Grafico01"/>
<img src="./imgs/Graf02-Historigrama.jpg" alt="Grafico 02"/>
<img src="./imgs/Graf03-Evolução.jpg" alt="Grafico 03"/>

## Avaliação
<img src="./imgs/N1-Avaliação.jpg" alt="Página 01"/>
<img src="./imgs/N1-Avaliação-pg2.jpg" alt="Página 02"/>
<img src="./imgs/N1-Avaliação-pg3.jpg" alt="Página 03"/>