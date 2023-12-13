# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC Mini projeto - Técnicas de Programação I
# MAGIC  
# MAGIC Objetivo
# MAGIC Você tem a tarefa de criar uma simulação para um jogo de dados. Essa simulação tem como objetivo reunir estatísticas para analisar a justiça do jogo, possíveis resultados e fazer previsões sobre jogos futuros.
# MAGIC Desafios do Projeto
# MAGIC Simulação de Dados: Crie uma função que simule o lançamento de dois dados de seis lados (valores de 1 a 6). Esta função deve retornar a soma dos resultados dos dados.
# MAGIC Múltiplas Simulações: Use a função do passo 1 para simular um grande número de jogos de dados (digamos, 1000 jogos). Armazene o resultado de cada jogo em um array NumPy.
# MAGIC Análise de Dados: Agora, vamos analisar os resultados desses jogos. Calcule e imprima o seguinte:
# MAGIC A média dos resultados.
# MAGIC O lançamento máximo e mínimo.
# MAGIC O número de vezes que cada possível lançamento (2, 3, 4, 5, 6, 7, 8, 9, 10, 11 e 12) ocorreu.
# MAGIC Teste de Hipótese: Agora vamos fazer um pouco de teste de hipóteses:
# MAGIC Supondo um jogo justo (ou seja, todos os lançamentos são igualmente prováveis), o resultado da sua simulação coincide com essa suposição? Por que sim ou por que não?
# MAGIC O que isso significa para um jogador do jogo de dados?
# MAGIC Entregáveis
# MAGIC Um script Python (arquivo .py ou .ipynb) com a sua solução para os desafios apresentados.
# MAGIC Tempo de apresentação: A depender da quantidade de grupos. (Aproximadamente de 15 ~ 20 minutos)
# MAGIC
# MAGIC a entrega tem que ser atraves de link github 
# MAGIC

# COMMAND ----------

import pandas as pd

# Simulação de Dados: Crie uma função que simule o lançamento de dois dados de seis lados (valores de 1 a 6). Esta função deve retornar a soma dos resultados dos dados.
def simular_lancamento_dados():
    return pd.Series({'Resultado': sum([pd.Series({'Dado1': pd.Series([1, 2, 3, 4, 5, 6]).sample().values[0]}),
                                        pd.Series({'Dado2': pd.Series([1, 2, 3, 4, 5, 6]).sample().values[0]})])})

# Múltiplas Simulações: se a função do passo 1 para simular um grande número de jogos de dados (digamos, 1000 jogos). Armazene o resultado de cada jogo em um array NumPy.
num_simulacoes = 1000
resultados = pd.DataFrame([simular_lancamento_dados() for _ in range(num_simulacoes)])

# Análise de Dados: Agora, vamos analisar os resultados desses jogos. Calcule e imprima o seguinte:
media_resultados = resultados['Resultado'].mean()
maximo_resultado = resultados['Resultado'].max()
minimo_resultado = resultados['Resultado'].min()

print(f"Média dos resultados: {media_resultados:.2f}")  # A média dos resultados.
print(f"Lançamento máximo: {maximo_resultado}")  # O lançamento máximo.
print(f"Lançamento mínimo: {minimo_resultado}")  # O lançamento mínimo.

# Número de vezes que cada possível lançamento ocorreu
ocorrencias = resultados['Resultado'].value_counts().sort_index()
for i, count in ocorrencias.items():
    print(f"Lançamento {i}: {count} vezes")

# Teste de Hipótese
frequencia_esperada = num_simulacoes / 11
estatistica_chi_quadrado, _ = pd.testing.chisquare(ocorrencias, f_exp=[frequencia_esperada] * len(ocorrencias))

print("\nTeste de Hipótese:")
print(f"Estatística do Qui-Quadrado: {estatistica_chi_quadrado:.2f}")

# Interpretando os resultados do teste de hipótese
if estatistica_chi_quadrado < 16.92:  # Valor crítico para 95% de confiança com 10 graus de liberdade
    print("Não há evidências para rejeitar a hipótese nula. Os resultados coincidem com um jogo justo.")
else:
    print("Rejeitamos a hipótese nula. Os resultados não coincidem com um jogo justo.")

