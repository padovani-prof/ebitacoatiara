import pandas as pd

'''
    Cria um arquivo para cada ano com as linhas referentes a Itacoatiara apenas
'''

for ano in [2019, 2023]:
    print("Ano:", ano, end='', flush=True)
    df = pd.read_csv(f"..\\microdados_enem_{ano}\\DADOS\\MICRODADOS_ENEM_{ano}.csv", encoding='ISO-8859-1', delimiter=';', low_memory=False, dtype=str, keep_default_na=False)
    ita = df[df['CO_MUNICIPIO_ESC']=='1301902']
    ita.to_csv(f'MICRODADOS_ENEM_ITACOATIARA_{ano}.csv', sep=';', index=False, encoding='ISO-8859-1')
    print(" OK!", flush=True)