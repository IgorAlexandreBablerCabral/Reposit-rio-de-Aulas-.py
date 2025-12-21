import requests
from bs4 import BeautifulSoup

url ='https://python.org.br/web/'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

#Exibir o texto
print(extracao.text.strip())  #stip remove os espaços do codigo que esta sendo requisitado

#Filtrar a exibição pela tag
for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.text.strip()
    print('Titulo: ', titulo)

#Contar quantidade de titulos e paragrafos
contar_titulos = 0
contar_paragrafos =0

for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        contar_titulos +=1 #contar titulos = contar titulos +1
    elif linha_texto.name =='p':
        contar_paragrafos +=1

print('Total de Titulos', contar_titulos)
print('Total de paragrafos', contar_paragrafos)


