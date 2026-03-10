import pandas as pd

df = pd.read_csv('C:/Users/Igor/Documents/EBAC/clientes-v2.csv')

print(df.head().to_string())
print(df.tail().to_string())
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y' , errors='coerce')

print('Verificação Inicial')
print(df.info())

print('Analise de Dados Nulos: \n' , df.isnull().sum())
print('% de Dados nulos : \n' , df.isnull().mean() * 100)
df.dropna(inplace=True)
print('Confirmar remoção de dados nulos:\n ' , df.isnull().sum().sum())

print('Analise de dados únicos: \n' ,df.nunique())

print('Estatistica dos dados: \n ' , df.describe())

df = df [['idade','data','estado','salario','nivel_educacao','numeros_filhos','estado_civil','area_atuacao']]

df.to_csv('clientes-v2-tratados.csv', index=False)









