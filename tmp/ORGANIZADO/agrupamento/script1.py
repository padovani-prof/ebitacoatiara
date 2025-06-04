import pandas as pd

df_pib = pd.read_excel('IBGE_pib.xlsx')
df_pib = df_pib[df_pib['Ano'] == 2021]
df_pib['CO_MUN'] = df_pib['Código do Município']
df_pib['PIB_PER_CAPITA'] = df_pib['Produto Interno Bruto per capita, \na preços correntes\n(R$ 1,00)']
df_pib = df_pib[['CO_MUN', 'PIB_PER_CAPITA']]
df_pib.to_csv('resumo_pib.csv', index=False, encoding='Cp1252', sep=';')

df_censo = pd.read_csv('IBGE_populacao.csv', encoding='Cp1252', delimiter=';')
df_censo['CO_MUN'] = df_censo['CD_MUN']
df_censo['NO_MUN'] = df_censo['NM_MUN']
df_censo['NO_UF'] = df_censo['NM_UF']
df_censo['POPULACAO'] = df_censo['v0001']
df_censo['DOMICILIOS'] = df_censo['v0002']
df_censo = df_censo[['CO_MUN', 'NO_MUN', 'NO_UF', 'POPULACAO', 'DOMICILIOS']]
df_censo.to_csv('resumo_censo.csv', index=False, encoding='Cp1252', sep=';')

df_idh = pd.read_csv('idh.csv', delimiter=';', encoding='Cp1252')
df_idh['IDH'] = df_idh['IDHM 2010'].str.replace(',', '.').astype(float)
df_idh = df_idh[['CO_MUN', 'IDH']]
df_idh.to_csv('resumo_idh.csv', index=False, encoding='Cp1252', sep=';')

df_final = pd.merge(df_censo, df_pib, on='CO_MUN', how='inner')
df_final = pd.merge(df_final, df_idh, on='CO_MUN', how='inner')
df_final.to_csv('resumo_total.csv', index=False, encoding='Cp1252', sep=';')
