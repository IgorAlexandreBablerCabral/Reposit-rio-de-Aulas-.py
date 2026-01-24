import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('Cliente_remove_outliers.csv')

print(df.head())
#mascarar dados pessoais
df['cpf_mascara'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2:]}') #nese código vai mostrar os 3 primeiros caracteres fazer as ***-*** e mostrar os  dois ultimos

#corrigir Datas
df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d', errors='coerce')

data_atual = pd.to_datetime('today')
df['data_atualizada'] = df ['data'].where(df['data'] <= data_atual, pd.to_datetime('1900-01-01'))
df['idade_ajustada'] = data_atual.year - df['data_atualizada'].dt.year
df['idade_ajustada'] -= ((data_atual.month <= df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int)
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan

#corrigir campo com múltiplas informações

df['endereço_curto'] = df['endereço'].apply(lambda x: x.split('\n')[0].strip())
df['bairro'] = df['endereço'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n')) >1 else 'Desconhecido')
df['estado_sigla'] = df['endereço'].apply(lambda x: x.split('/')[-1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')

#Verificando a formatação do endereço
df['endereço_curto'] = df['endereço_curto'].apply(lambda x: 'Endereço Inválido' if len(x) > 50 or len(x) <5 else x)

#Corrigir dados erroneos
df['cpf'] = df['cpf'].apply (lambda x: x if len(x) == 14 else 'CPF Inválido')

estados_br = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
df['estado_sigla'] = df['estado_sigla'].str.upper().apply(lambda x: x if x in estados_br else 'Desconhecido')

print('Dados tratados:\n' , df.head())

df['cpf'] = df['cpf_mascara']
df['idade'] = df['idade_ajustada']
df['endereço'] = df['endereço_curto']
df['estado'] = df['estado_sigla']
df_salvar = df[['nome' , 'cpf', 'idade', 'endereço', 'estado']]
df_salvar.to_csv('clientes_tratados.csv', index=False)

