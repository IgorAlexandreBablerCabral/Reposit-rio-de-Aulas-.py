import pandas as pd

df = pd.read_csv('C:/Users/Igor Blaer Cabral/Downloads/clientes.csv')

pd.set_option('display.width', None)
print(df.head())

#remover dados
df.drop('pais' , axis=1, inplace=True) #Coluna Axis=1 é referente a coluna
df.drop(2 , axis=0, inplace=True) #Linha Axis=0 é referente a linha

#normalizar campos de texto

df['nome'] = df['nome'].str.title()   # com Str.Title todas as primeiras letras ficam Maiusculas
df['endereço'] = df['endereco'].str.lower() # com lower Tudo fica Minusculo
df['estado'] = df['estado'].str.strip().str.upper() # com upper tudo fica maiusculo

# Converter tipos de dados
df['idade'] = df['idade'].astype(int) #normalizando os dados, convertendo idade para numeros inteiros !IMPORTANTE PARA A LIMPEZA

#Tratar valores nulos (ausentes)

df_fillna = df.fillna(0) #Substituir valores nulos por 0
df_dropna = df.dropna()  #Remover registros com valores nulos
df_dropna4 = df.dropna(thresh=4) #Manter registro com no minimo 4 valores não nulos
df = df.dropna(subset=['cpf']) #Remover registros de cpf nulo

print('Valores nulos: \n' , df.isnull().sum())
print('Qtd de registros nulos com fillna:', df_fillna.isnull().sum().sum())
print('Qtd de registros nulos com dropna:' , df_dropna.isnull().sum().sum())
print('Qtd de registros nulos com dropna4:' , df_dropna4.isnull().sum().sum())
print('Qtd de registros nulos com CPF:' , df.isnull().sum().sum())

df.fillna({'estado': 'Desconhecido'}, inplace=True)
df['endereço'] = df['endereco'].fillna('Endereço não informado') # mesma resolução da linha de cima, sendo executada de outra forma
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())   # mean é a média, ele esta capturando a media da idade

#Tratar Formato de Dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y' , errors='coerce')

#Tratar dados duplicados
print('Qtd registros atuais:' , df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True) #cpfs duplicados devem ser removidos por hora nesse exercicio
print('Qtd registros removendo as duplicatas' , len(df))

print('Dados Limpos:' , df)

#Salvando dataframe
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome' , 'cpf' , 'idade' , 'data' , 'endereço' , 'estado']]
df_salvar.to_csv('clientes_limpeza.csv' , index=False)

print('Novo Dataframe: \n' , pd.read_csv('clientes_limpeza.csv'))




