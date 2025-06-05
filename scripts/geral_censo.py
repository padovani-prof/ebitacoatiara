import pandas as pd

def carregar_csv(arquivo):
    return pd.read_csv(arquivo, encoding='ISO-8859-1', delimiter=';', low_memory=False, dtype=str, keep_default_na=False)

def carregar_dados_totais(anos = [2018, 2019, 2022, 2023], prefixoLeitura="../dados/originais/microdados_ed_basica_"):
    print("TOTAIS: Carregando dados totais...", flush=True)
    retorno = {}
    for ano in anos:
        print(f"TOTAIS: Ano: {ano}...", flush=True, end='')
        df = carregar_csv(f"{prefixoLeitura}{ano}.csv")
        retorno[ano] = df
        print(" OK!", flush=True)
    return retorno

def carregar_dados_ita(anos = [2018, 2019, 2022, 2023], prefixoLeitura = '../dados/MD_CENSO_ITA_'):
    print("ITA: Carregando dados da Itacoatiara...", flush=True)
    retorno = {}
    if prefixoLeitura is None:
        totais = carregar_dados_totais(anos)
        for ano, df in totais.items():
            print(f"ITA: Ano: {ano}...", flush=True, end='')
            df = df[df['CO_MUNICIPIO']=='1301902']
            retorno[ano] = df
            print(" OK!", flush=True)
    else:
        for ano in anos:
            print(f"ITA: Ano: {ano}...", flush=True, end='')
            retorno[ano] = carregar_csv(f"{prefixoLeitura}{ano}.csv")
            print(" OK!", flush=True)
    return retorno

def salvar_dados_ita(anos = [2018, 2019, 2022, 2023], prefixoEscrita = '../dados/MD_CENSO_ITA_'):
    print("ITA: Salvando dados da Itacoatiara...", flush=True)
    retorno = {}
    ita = carregar_dados_ita(anos, None)
    for ano, df in ita.items():
        print(f"ITA: Ano: {ano}...", flush=True, end='')
        df.to_csv(f'{prefixoEscrita}{ano}.csv', sep=';', index=False, encoding='ISO-8859-1')
        print(" OK!", flush=True)

