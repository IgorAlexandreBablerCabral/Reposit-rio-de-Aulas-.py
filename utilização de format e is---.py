Nome = raw_input('Digite o seu nome')

print('seu nome e {}'.format(Nome))

# Adicao de variaveis pelo print('texto {}'.format(Variavel Indicada no {}))

print ('____________________________________________________________________')
# Lembre-se para qualquer variavel se tornar um numero voce precisa utilizar int ou float

n = raw_input('Bom Dia!! Qual o seu nome?')
print('Bem vindo {} escolha dois numeros para somar'.format(n))
n1 = int(raw_input('Digite o primeiro numero!'))
n2 = int(raw_input('Agora digite o segundo numero numero!'))
s = (n1+n2)

print('A soma entre {} e {} resulta a {}'.format(n1, n2, s))
print ('Tenha um otimo dia!')

print ('_____________________________________________________________________')

# Exercicio para ler uma caixa input e mostrar todos os formatos que aquela text box possui

z = raw_input('Ola {} Digite algo e mostrarei todos os formatos logicos de seus caracteres digitados!'.format(n))

print ('o tipo primitivo da text box e', type(z))
print ('minha text box e so espaco?', z.isspace())
print ('minha text box e um titulo?', z.istitle())
print ('minha text box e toda maiuscula?', z.isupper())
print ('minha text box e somente alfabetica?', z.isalpha())
print ('minha text box sao so digitos', z.isdigit())
print ('minha text box e alfanumerico', z.isalnum())

