import requests


def enviar_arquivos():

    caminho = 'C:\Users\Igor Blaer Cabral\Pictures\Screenshots\Captura de tela 2025-06-22 234324.png' #Caminho do arquivo para upload

    requisicao = requests.post('https://file.io' , files={'file': open(caminho, 'rb')}) #mandando o arquivo rb (R = read/leitura) (B = Binary/Binario) || Esta enviando (Request.Post para a  url que esta no comando)
    saida_requisicao = requisicao.json() #Tranformando a Saida em Json

    print(saida_requisicao)
    url = saida_requisicao['url']
    print("Arquivo enviado. Link para acesso:", url)



def enviar_arquivos_chave():
    #Caminho do Arquivo e chave para upload
    caminho ='C:\Users\Igor Blaer Cabral\Pictures\Screenshots\Captura de tela 2025-06-22 234324.png'


