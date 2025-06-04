import pandas as pd

'''
Extrai dados de Itacoatiara (CO_MUNICIPIO=1301902)
Arquivo: ce_ita_semiguais_<ano>.csv
Salva os nomes das colunas restantes em colunas_interesse_ita_semiguais.csv
'''

print("ANO\tIGUAIS")
unicos = {}
for ano in [2018, 2019, 2022, 2023]:
    df = pd.read_csv(f"ce_ita_todas_{ano}.csv", encoding='ISO-8859-1', delimiter=';', low_memory=False)
    colunas_unico_valor = list(df.columns[df.nunique() == 1])
    valores_unicos = {col: df[col].iloc[0] for col in colunas_unico_valor}
    unicos[ano] = valores_unicos
    print(ano, len(valores_unicos), sep='\t')
    
valores_iguais = set(unicos[2018].keys()) & \
        set(unicos[2019].keys()) & \
        set(unicos[2022].keys()) & \
        set(unicos[2023].keys())

colunas_para_remover = []
for valor in valores_iguais:
    if unicos[2018][valor] == unicos[2019][valor] == unicos[2022][valor] == unicos[2023][valor]:
      colunas_para_remover.append(valor)
print("Colunas a remover:", len(colunas_para_remover))

for ano in [2018, 2019, 2022, 2023]:
    df = pd.read_csv(f"ce_ita_todas_{ano}.csv", encoding='ISO-8859-1', delimiter=';', low_memory=False)
    df_sem_colunas = df.drop(columns=colunas_para_remover)
    df_sem_colunas.to_csv(f"ce_ita_semiguais_{ano}.csv", index=False, sep=';')

print("Colunas restantes:", len(df_sem_colunas.columns))
print("Nomes salvos em colunas_interesse_ita_semiguais.csv")
df = pd.DataFrame(df_sem_colunas.columns, columns=["Nome"])
df.to_csv("colunas_interesse_ita_semiguais.csv", index=False)