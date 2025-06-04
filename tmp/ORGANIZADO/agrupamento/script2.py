import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import math

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

# Aplicando técnica do Cotovelo
distancias = []

K = range(2, 20)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=1902, n_init=10)
    labels = kmeans.fit_predict(X_weighted)  # usa fit_predict para pegar labels direto
    distancias.append(kmeans.inertia_) # soma das distâncias dos pontos do cluster

print("K (Sturges):", K_Sturges)
    
# Plotando o cotovelo
plt.figure(figsize=(8, 5))
plt.plot(K, distancias, 'bo-')
plt.xlabel('Número de Clusters')
plt.ylabel('distancias')
plt.title('Método do Cotovelo')
plt.show()


