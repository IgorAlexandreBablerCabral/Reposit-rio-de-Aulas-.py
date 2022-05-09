# Programa que le a media de um aluno

Aluno = raw_input('Bom dia aluno qual o seu nome?')
print ('como vai {}, para saber suas notas prossiga com as seguintes informacoes!'.format(Aluno))
nota_1 = float(raw_input('{} qual foi sua nota da P1?'.format(Aluno)))
nota_2 = float(raw_input('{} qual foi sua nota da P2?'.format(Aluno)))
media = (nota_1+nota_2)/2

print ('Ola {} sua nota final e de {}'.format(Aluno, media))

print ('_'*70)

Metragem = float(raw_input('Agora {} escolha aleatoriamente uma metragem para ser convertida em centimetros e '
                           'milimetros'''.format(Aluno)))
print ('Bem... {} nao que faca muito sentido mas essa metragem deu {} centimetros e {} milimetros'
       .format(Aluno, Metragem*100, Metragem*1000))

print raw_input('Ou {} vamo lanca de uma tabuada do nada? fdc!'.format(Aluno))

numero = int(raw_input('entao lanca lancante qual o numerosco da que voce quer a tabueida?? (pode escrever so '
                       'o numero o animal!)'))

print ('Ai papai ta na mao BAW '
       '{}x1={} '
       '{}x2={} '
       '{}x3={} '
       '{}x4={} '
       '{}x5={} '
       '{}x6={} '
       '{}x7={} '
       '{}x8={} '
       '{}x9={} '
       '{}x10={} '
       'TIREI ONDA OU NUM TIREI??!! BAW! BAW!'.format(numero, numero*1, numero, numero*2, numero, numero*3, numero,
                                                      numero*4, numero, numero*5, numero, numero*6, numero,
                                                      numero*7, numero, numero*8, numero, numero*9, numero, numero*10,))
