'''
Para cada ano do enem, identifica:
- Quantidade de colunas no dicionário de dados
- Quantidade de colunas no dataset
- Quantidade de colunas comuns em todos os datasets e dicionários
Salva colunas em colunas_comuns_enem.csv
'''

import pandas as pd
import os

print("ANO\tTOTAL\tDATASET")

contador_colunas = {}
for ano in [2018, 2019, 2022, 2023]:
  df = pd.read_excel(f"D:\\Arquivos\\Downloads\\GPA\\microdados_enem_{ano}\\DICIONÁRIO\\Dicionário_Microdados_Enem_{ano}.xlsx", usecols=[0,1], skiprows=5, header=None)
  df = df.dropna()
  colunas_dicionario = list(df[0])
  colunas_dicionario = list(map(lambda x: x.upper().strip(), colunas_dicionario))
  total_dic = len(colunas_dicionario)
  df = pd.read_csv(f"microdados_enem_{ano}\\DADOS\\MICRODADOS_ENEM_{ano}.csv", encoding='ISO-8859-1', delimiter=';', low_memory=False, nrows=1)
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
df.to_csv("colunas_comuns_enem.csv", index=False)
print("Colunas comuns salvas em colunas_comuns_enem.csv")
 