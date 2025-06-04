'''
Remove as colunas não comuns dos arquivos do enem, salvando o resultado em
enem_cc_<ano>.csv
'''
import pandas as pd
import csv
import gc
import sys

with open('colunas_comuns_enem.csv') as t:
  colunas_comuns = t.readlines()
  del colunas_comuns[0]
  colunas_comuns = list(map(lambda x: x.strip(), colunas_comuns))
  
for ano in [2018, 2019, 2022, 2023]:
  df = pd.read_csv(f"microdados_enem_{ano}\\DADOS\\MICRODADOS_ENEM_{ano}.csv", encoding='ISO-8859-1', delimiter=';', low_memory=False, usecols=colunas_comuns)
  df.to_csv(f"enem_cc_{ano}.csv", index=False, sep=';')
  del df
  gc.collect()