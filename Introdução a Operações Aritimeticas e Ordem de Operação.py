# Nas operacoes aritimeticas temos operadores e prioridades os operadores sao

# + adicao    ex: 5+2 == 7

# - subtracao ex: 5-2 == 3

# * multiplicacaco 5*2 == 10

# / divisao        5/2 == 2.5

# ** potencializacao (potencia) 5**2 == 25

# %  modulo (resto da divisao)  5%2 == 1

# // divisao inteira 5//2 == 2

# print ('____________________________________________________________')

# Ordem de Prioridade para operacoes matematicas

# 1-()
# 2- **(potencias)
# 3- *, /, //, %   (multiplicacao, divisao, divisao inteira, modulo ou resto da divisao
# 4- + -

nome = raw_input('Ola, qual o seu nome?')
print ('Ola {}'.format(nome))
print ('Escolha dois numeros para que possamos fazer todas as operacoes matematicas com ambos!!')
n1 = float(raw_input('Digite o primeiro numero'))
n2 = float(raw_input('Agora digite o segundo numero'))
ant_n1 = n1-1
suss_n1 = n1+1
ant_n2 = n2-1
suss_n2 = n2+1
dobro_n1 = n1*2
triplo_n1 = n1*3
raiz_n1 = n1*n1
dobro_n2 = n2*2
triplo_n2 = n2*3
raiz_n2 = n2*n2

print ('A soma entre os dois numeros e de {}, a subtracao entre os dois numeros e de {}, a multiplicacao dos '
       'numeros e de {}, a divisao e de {} o resto da divisao e de {}, a potencializacao e de {} a divisao '
       'inteira e de {}'
       ''.format(n1+n2, n1-n2, n1*n2, n1/n2, n1 % n2, n1**n2, n1//n2))

print ('_'*60)

print ('Ola novamente {}'.format(nome))
print ('Sabia que o antecessor do seu primeiro numero era {} e o antecessor do seu segundo numero era {}?'
       ' por vez os sucessores deles eram {} e {} ! nessa ordem' .format(ant_n1, ant_n2, suss_n1, suss_n2))

print ('O dobro de seu primeiro numero era {} o triplo do seu primeiro numero era {} e a raiz quadrade dele era {}.'
       ' Na mesma sequencia do segundo numero temos dobro {}, triplo {} e '
       'raiz {}.'.format(dobro_n1, triplo_n1, raiz_n1, dobro_n2, triplo_n2, raiz_n2))
