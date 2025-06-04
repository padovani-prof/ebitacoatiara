'''
Remove as colunas não comuns dos arquivos do censo, salvando o resultado em
ce_cc_<ano>.csv
'''
import pandas as pd
import csv
import gc
import sys

with open('colunas_comuns.csv') as t:
  colunas_comuns = t.readlines()
  del colunas_comuns[0]
  colunas_comuns = list(map(lambda x: x.strip(), colunas_comuns))
  
for ano in [2018, 2019, 2022, 2023]:
  df = pd.read_csv(f"microdados_censo_escolar_{ano}/dados/microdados_ed_basica_{ano}.csv", encoding='ISO-8859-1', delimiter=';', low_memory=False, usecols=colunas_comuns)
  df.to_csv(f"ce_cc_{ano}.csv", index=False, sep=';')
  del df
  gc.collect()