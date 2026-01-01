import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('C:/Users/Igor Blaer Cabral/Downloads/clientes_limpeza.csv')

df_filtro_basico = df[df['idade']>100]

print('Filtro básico \n' , df_filtro_basico[['nome','idade']])

#Identificar outliers com Z-score
z_score = stats.zscore(df['idade'].dropna())
outliers_z = df[z_score >= 3]
print("Outliers Z-score: \n" , outliers_z)

#Filtrar outliers com Z-score
df_zscore = df[(stats.zscore(df['idade']) <3)]

# Identificar outliers com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print("Limites IQR: ", limite_baixo, limite_alto)

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print("Outliers pelo IQR:\n", outliers_iqr)

# Filtrar outliers com IQR
df_iqr = df[(df['idade'] >= limite_alto) & (df['idade'] <= limite_alto)]

limite_baixo = 1
limite_alto = 100
df = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

#filtrar endereços invalidos
df['endereço'] = df['endereço'].apply(lambda x:'endereço invalido' if len(x.split('\n')) <3 else x)

#tratar campos de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome Invalido' if isinstance(x, str) and len(x) > 50 else x)
print('Qtd de registros com nome grandes: ', (df['nome'] == 'Nome Inválido').sum())

print('Dados com Outliers tratados: \n' , df)

#Salvar Dataframe
df.to_csv('Cliente_remove_outliers.csv',index=False)

#TESTE GIT FUNCIONA



