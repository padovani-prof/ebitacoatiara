import pandas as pd

'''
Extrai dados de Itacoatiara (CO_MUNICIPIO=1301902)
Arquivo: enem_ita_todas_<ano>.csv
'''

print("ANO\tQTD")
for ano in [2018, 2019, 2022, 2023]:
    df = pd.read_csv(f"enem_cc_{ano}.csv", encoding='ISO-8859-1', delimiter=';', low_memory=False)
    df = df[df['CO_MUNICIPIO_ESC'] == 1301902]
    print(ano, len(df), sep='\t')
    df.to_csv(f"enem_ita_todas_{ano}.csv", index=False, sep=';')
