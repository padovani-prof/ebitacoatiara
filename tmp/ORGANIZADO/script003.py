import pandas as pd

'''
    Redefine o sequencial do número da questão na planilha das questões das provas.
'''

for ano in [2019, 2023]:
    df = pd.read_csv(f"..\\microdados_enem_{ano}\\DADOS\\ITENS_PROVA_{ano}.csv", encoding='ISO-8859-1', delimiter=';', low_memory=False, dtype=str, keep_default_na=False)
    df['CO_POSICAO'] = df["CO_POSICAO"].astype(int)
    df = df.sort_values(by=["CO_PROVA", "CO_POSICAO"]).reset_index(drop=True)
    df["NU_POSICAO"] = df.groupby("CO_PROVA")["CO_POSICAO"].rank(method="dense").astype(int)
    df.to_csv(f'ITENS_PROVA_POSICAO_{ano}.csv', sep=';', index=False, encoding='ISO-8859-1')
