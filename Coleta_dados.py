import requests
from bs4 import BeautifulSoup
import pandas

print('Request: ')
response = requests.get('https://www.worldometers.info/world-population/population-by-country/') # esse é o comando que faz uma variavel pushar os dados de um site
print(response.text[:700]) # esta pushando 700 caracteres do site que estamos pushando as infos

soup = BeautifulSoup(response.text,'html.parser')
print(soup.prettify()[:1000])

print('Pandas: ')
url_dados = pandas.read_html('https://www.worldometers.info/world-population/population-by-country/')
print(url_dados[0].head(10))

