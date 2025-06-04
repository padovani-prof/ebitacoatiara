import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import math
from sklearn.metrics import pairwise_distances

top_n = 5 # quantidade de próximos
df_final = pd.read_csv('resumo_total.csv', encoding='Cp1252', delimiter=';')
df_final['POPULACAO'] = df_final['POPULACAO'].astype(float)
df_final['DOMICILIOS'] = df_final['DOMICILIOS'].astype(float)
df_final['PIB_PER_CAPITA'] = df_final['PIB_PER_CAPITA'].astype(float)
df_final['IDH'] = df_final['IDH'].astype(float)

X = df_final[['POPULACAO', 'DOMICILIOS', 'PIB_PER_CAPITA', 'IDH']]

K_Sturges = int(round(1 + math.log2(len(X))))

# Padronizando valores (para ficarem em escalas similares e um 
# não 'puxar' mais que o outro pela magnitude)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicação dos pesos (IDH com peso 1 e demais com peso 3
weights = [0.3, 0.3, 0.3, 0.1]
X_weighted = X_scaled * weights

k = K_Sturges
kmeans = KMeans(n_clusters=k, random_state=1902, n_init=10)
labels = kmeans.fit_predict(X_weighted)  # para pegar labels/grupos de cada cidade

df_final['cluster'] = labels
idx_cidade = df_final.index[df_final['CO_MUN'] == 1301902][0] # linha onde está Itacoatiara
label_cluster_ita = df_final.loc[idx_cidade, 'cluster'] # label de Itacoatiara
df_cluster_ita = df_final[df_final['cluster'] == label_cluster_ita] # municípios do grupo de Itacoatiara

vetor_alvo = X_weighted[idx_cidade].reshape(1, -1) # dados normalizados de Itacoatiara (em vetor)
indices_cluster = df_cluster_ita.index.tolist() # pega os índices de cada cidade do cluster
matriz_cluster = X_weighted[indices_cluster] # dados normalizados de todas as cidades do cluster

distancias = pairwise_distances(vetor_alvo, matriz_cluster).flatten() # calcula distâncias

idx_distancias = list(zip(indices_cluster, distancias)) # junta os índices com as distâncias de Ita
idx_distancias = [x for x in idx_distancias if x[0] != idx_cidade] # remove Ita da lista
idx_distancias.sort(key=lambda x: x[1]) # ordena pela distância
tops = idx_distancias[:top_n] # pega os 'top' mais próximos


print("POPULACAO;PIB;IDH;DOMICILIOS;DISTANCIA;CO_MUN;NO_MUN;NO_UF")
idx = idx_cidade
dist = 0.0
print(f"{df_final.loc[idx, 'POPULACAO']};{df_final.loc[idx, 'PIB_PER_CAPITA']};{df_final.loc[idx, 'IDH']};{df_final.loc[idx, 'DOMICILIOS']};{dist:.4f};{df_final.loc[idx, 'CO_MUN']};{df_final.loc[idx, 'NO_MUN']};{df_final.loc[idx, 'NO_UF']}")
for idx, dist in tops:
    print(f"{df_final.loc[idx, 'POPULACAO']};{df_final.loc[idx, 'PIB_PER_CAPITA']};{df_final.loc[idx, 'IDH']};{df_final.loc[idx, 'DOMICILIOS']};{dist:.4f};{df_final.loc[idx, 'CO_MUN']};{df_final.loc[idx, 'NO_MUN']};{df_final.loc[idx, 'NO_UF']}")
    

