# Databricks notebook source
# MAGIC %md
# MAGIC # Hands-On
# MAGIC
# MAGIC Você foi designado para realizar a limpeza e preparação de dados de dois conjuntos de dados (base1.csv e base2.csv) distintos que representam informações relacionadas a risco de crédito.
# MAGIC
# MAGIC Seu objetivo é ler os dois conjuntos de dados usando a biblioteca Pandas, realizar a concatenação dos dados, lidar com valores duplicados e faltantes, além de verificar a presença de outliers nos dados combinados.
# MAGIC
# MAGIC ____
# MAGIC
# MAGIC ## Passos a serem seguidos:
# MAGIC
# MAGIC 1. **Leitura dos Arquivos:** Utilize a biblioteca Pandas para ler os dois arquivos de dados: 'base1.csv' e 'base2.csv', que estão no diretório datasets, no repositório do módulo.
# MAGIC 2. **Concatenação dos Dados:** Concatene os dois conjuntos de dados em um único DataFrame, verificando se os dados possuem a mesma estrutura para uma concatenação adequada.
# MAGIC 3. **Tratamento de Dados Duplicados:** Verifique se há linhas duplicadas no DataFrame combinado e remova-as, mantendo a primeira ocorrência.
# MAGIC 4. **Tratamento de Valores Faltantes:** Identifique e lide com os valores faltantes no DataFrame combinado. Preencha os valores ausentes com estratégias apropriadas (média, mediana, valor específico etc.) dependendo do contexto dos dados.
# MAGIC 5. **Verificação de Outliers:** Utilize métodos estatísticos ou gráficos (como boxplots) para identificar a presença de outliers nos dados. Considere se eles são significativos para a análise ou se precisam ser tratados de alguma forma.

# COMMAND ----------

import pandas as pd

# 1. **Leitura dos Arquivos:** Utilize a biblioteca Pandas para ler os dois arquivos de dados: 'base1.csv' e 'base2.csv', que estão no diretório datasets, no repositório do módulo.

base1 = pd.read_csv('/Workspace/Repos/allanb@unimedcampinas.com.br/ADA_classes/DS-PY-Data-Science/DS-PY-004 TÉCNICAS DE PROGRAMAÇÃO I (PY)/Material do Aluno/datasets/base1.csv')
base2 = pd.read_csv('/Workspace/Repos/allanb@unimedcampinas.com.br/ADA_classes/DS-PY-Data-Science/DS-PY-004 TÉCNICAS DE PROGRAMAÇÃO I (PY)/Material do Aluno/datasets/base2.csv')

print(base1)

# COMMAND ----------

# 2. **Concatenação dos Dados:** Concatene os dois conjuntos de dados em um único DataFrame, verificando se os dados possuem a mesma estrutura para uma concatenação adequada.

bases_concatenadas = pd.concat([base1, base2], ignore_index=True)

print(bases_concatenadas.head())

# COMMAND ----------

# 3. **Tratamento de Dados Duplicados:** Verifique se há linhas duplicadas no DataFrame combinado e remova-as, mantendo a primeira ocorrência.

bases_concatenadas_sem_duplicatas = bases_concatenadas.drop_duplicates()

print(bases_concatenadas_sem_duplicatas.head())

# COMMAND ----------

# 4. **Tratamento de Valores Faltantes:** Identifique e lide com os valores faltantes no DataFrame combinado. Preencha os valores ausentes com estratégias apropriadas (média, mediana, valor específico etc.) dependendo do contexto dos dados.

# Substituindo os valores faltantes com a média
bases_concatenadas_preenchidas = bases_concatenadas.fillna(bases_concatenadas.mean())

# Verificando se ainda tem valores faltantes após o tratamento
print("\nValores faltantes após o tratamento:")
print(bases_concatenadas_preenchidas.isnull().sum())

print(bases_concatenadas_preenchidas.head())


# COMMAND ----------

# 5. **Verificação de Outliers:** Utilize métodos estatísticos ou gráficos (como boxplots) para identificar a presença de outliers nos dados. Considere se eles são significativos para a análise ou se precisam ser tratados de alguma forma.

import matplotlib.pyplot as plt

bases_concatenadas_preenchidas.boxplot()
plt.title('Boxplot das colunas')
plt.xlabel('Grupos')
plt.ylabel('Valores')
plt.show()

def identificar_outliers(df, coluna):
    # Calculando o primeiro e terceiro quartis
    Q1 = df[coluna].quantile(0.25) #Primeiro Quartil
    Q3 = df[coluna].quantile(0.75) #Terceiro Quartil
    
    # Calculando o IQR (Intervalo Interquartil)
    IQR = Q3 - Q1
    
    # Calculando os limites superior e inferior para identificar os outliers
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    # Identificando outliers na coluna especificada
    outliers = df[(df[coluna] < limite_inferior) | (df[coluna] > limite_superior)]
    
    return outliers
