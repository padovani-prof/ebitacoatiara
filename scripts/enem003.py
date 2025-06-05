import enem_geral as enem
import pandas as pd

dataframes = enem.carregar_dados_ita()

provas = {
    'CN': 'TP_PRESENCA_CN',
    'CH': 'TP_PRESENCA_CH',
    'LC': 'TP_PRESENCA_LC',
    'MT': 'TP_PRESENCA_MT',
    'RD': 'NU_NOTA_REDACAO'
}

resultado = pd.DataFrame(index=provas.keys(), columns=dataframes.keys())

for ano, df in dataframes.items():
    total_alunos = len(df)
    
    for prova, coluna in provas.items():
        if prova != 'RD': 
            presentes = (df[coluna] == '1').sum()
        else:
            presentes = (df[coluna] != '').sum()
        
        percentual = presentes / total_alunos
        resultado.at[prova, ano] = percentual

resultado = resultado.map(lambda x: round(x, 5))

print(resultado)
