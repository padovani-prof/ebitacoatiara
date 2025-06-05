import enem_geral as enem

'''
	Obtém quantidades de inscritos ao longo dos anos
'''

ita = enem.carregar_dados_ita()
for ano, df in ita.items():
    print("Ano:", ano, "Qtd.:", len(df))