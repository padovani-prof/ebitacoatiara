'''
Para cada ano do censo, identifica:
- Quantidade de colunas no dicionário de dados
- Quantidade de colunas no dataset
- Quantidade de colunas comuns em todos os datasets e dicionários
Salva colunas em colunas_comuns.csv
'''

import pandas as pd
import os

print("ANO\tTOTAL\tDATASET")

contador_colunas = {}
for ano in [2018, 2019, 2022, 2023]:
  df = pd.read_excel(f"microdados_censo_escolar_{ano}\\Anexos\\ANEXO I - Dicionário de Dados\\dicionário_dados_educação_básica.xlsx", usecols=[1], skiprows=9, header=None)
  df = df.dropna()
  colunas_dicionario = list(df[1])
  colunas_dicionario = list(map(lambda x: x.upper().strip(), colunas_dicionario))
  total_dic = len(colunas_dicionario)
  df = pd.read_csv(f"microdados_censo_escolar_{ano}/dados/microdados_ed_basica_{ano}.csv", encoding='ISO-8859-1', delimiter=';', low_memory=False, nrows=1)
  colunas_dataset = []
  for coluna in map(lambda x: x.upper().strip(), list(df.columns)):
    if coluna in colunas_dicionario:
        colunas_dataset.append(coluna)
        contador_colunas[coluna] = contador_colunas.get(coluna, 0) + 1
  total_ds = len(colunas_dataset)
  print(ano, total_dic, total_ds, sep='\t')
colunas_comuns = dict(filter(lambda v: v[1] == 4, contador_colunas.items()))
print("Colunas comuns:", len(colunas_comuns))
df = pd.DataFrame(colunas_comuns.keys(), columns=["Nome"])
df.to_csv("colunas_comuns.csv", index=False)
print("Colunas comuns salvas em colunas_comuns.csv")
 