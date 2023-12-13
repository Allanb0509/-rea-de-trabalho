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
import numpy as np

# Simulação de Dados: Crie uma função que simule o lançamento de dois dados de seis lados (valores de 1 a 6). Esta função deve retornar a soma dos resultados dos dados.
def simular_lancamento_dados():
    dado1 = np.random.choice([1, 2, 3, 4, 5, 6])
    dado2 = np.random.choice([1, 2, 3, 4, 5, 6])
    return dado1 + dado2

# Múltiplas Simulações: se a função do passo 1 para simular um grande número de jogos de dados (digamos, 1000 jogos). Armazene o resultado de cada jogo em um array NumPy.
num_simulacoes = 1000
resultados = pd.DataFrame([simular_lancamento_dados() for _ in range(num_simulacoes)], columns=['Resultado'])

# Número de vezes que cada possível lançamento ocorreu
ocorrencias = resultados['Resultado'].value_counts().sort_index()
for i, count in ocorrencias.items():
    print(f"Lançamento {i}: {count} vezes")

# Teste de Hipótese sem o uso de scipy.stats
frequencia_esperada = num_simulacoes / 11
diferenca_quadratica = ((ocorrencias - frequencia_esperada) ** 2) / frequencia_esperada
estatistica_chi_quadrado = diferenca_quadratica.sum()

print("\nTeste de Hipótese:")
print(f"Estatística do Qui-Quadrado: {estatistica_chi_quadrado:.2f}")

# Interpretando os resultados do teste de hipótese
graus_de_liberdade = len(ocorrencias) - 1
valor_critico = np.percentile(np.random.chisquare(df=graus_de_liberdade, size=10000), 95)
if estatistica_chi_quadrado < valor_critico:
    print("Não há evidências para rejeitar a hipótese nula. Os resultados coincidem com um jogo justo.")
else:
    print("Rejeitamos a hipótese nula. Os resultados não coincidem com um jogo justo.")


