#Estduos de Dataframe
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

#Lista: Uma coleção ordenada de elementos que podem ser de qualquer tipo
lista_nomes = {'Ana' , 'Marcos' , 'Carlos'}
lista_nomes = list(lista_nomes)
print('Lista de nomes: \n', lista_nomes)
print('Primeiro Elemento na Lista: \n ' , lista_nomes[0])

#Dicionario:Estrutura composta de pares chave-valor
dicionario_pessoa = {
    'Nome': 'Ana',
    'Idade': 20,
    'Cidade': 'São Paulo'
}
print('Dicionario de uma Pessoa: \n ' , dicionario_pessoa)
print('Atributos do Dicionario: \n ' , dicionario_pessoa.get('Nome'))

#Lista de dicionarios: Estrutura de dados que combina lista e dicionarios
dados = [
    {'Nome': 'Ana', 'Idade': 20 , 'Cidade': 'São Paulo' },
    {'Nome': 'Marcos', 'Idade': 25 , 'Cidade': 'Campos do Jordão' },
    {'Nome': 'Carlos', 'Idade': 22 , 'Cidade': 'Sumaré'},
]
#Dataframe :Estrutura Bidimensional
df = pd.DataFrame(dados)
print('DataFrame \n' , df)

# Selecionar Coluna
print(df['Nome'])

# Selecionar várias colunas
print(df[['Nome' , 'Idade']])

#Selecionar linhas pelo indice
print('Primeira linha \n' , df.iloc[0])

#Adicionar um novo Registro
df['Salário'] = [4100, 3600 , 5200]

# Adicionar um novo registro
df.loc[len(df)] = {
    'Nome': 'João',
    'Idade': 30,
    'Cidade': 'Santo',
    'Salário': 4400
}
print('DataFrame Atual \n' ,df)

#Removendo uma Coluna
df.drop('Salário', axis=1, inplace=True)

#Filtrando pessoas com mais de 29 anos por exemplo
filtro_idade =df[df['Idade'] > 29]
print('Filtro de idade \n' , filtro_idade)

#Salvando o dataframe em um arquivo CSV
df.to_csv('dados.csv' , index=False)


