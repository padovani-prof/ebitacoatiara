import pandas as pd

'''
    Adiciona as colunas TX_ACERTOS_XX para identificar se o aluno acertou ou errou
'''

for ano in [2019, 2023]:
    df = pd.read_csv(f"MICRODADOS_ENEM_ITACOATIARA_{ano}.csv", encoding='ISO-8859-1', delimiter=';', low_memory=False, dtype=str, keep_default_na=False)
    for area in ['CN', 'CH', 'LC', 'MT']:
        df[f"TX_ACERTOS_{area}"] = df.apply(
            lambda row: ''.join('1' if r == g else '0' for r, g in zip(row[f"TX_RESPOSTAS_{area}"], row[f"TX_GABARITO_{area}"])), axis=1
        )
    df.to_csv(f'MICRODADOS_ENEM_ITACOATIARA_ACERTOS_{ano}.csv', sep=';', index=False, encoding='ISO-8859-1')