Sr_Sra = raw_input('Bom dia!, voce se considera Sr. , Sra. , ou Srta.')
Nome = raw_input('Bom dia {} como deseja ser chamado?'.format(Sr_Sra))

raw_input('Prazer {} {} ,irei te apresentar o funcionamento do calculo de ganho em massa em apostas okay?'
          .format(Sr_Sra, Nome))
# Automacao de porcentagem de erro eu to maluco se eu sobrio ver isso e nao fizer sentido releva (te amo)


print ('_'*70)

print ('{} {}, o metodo de ganho e baseado no alto numero de apostas de baixo risco ou seja apostas que voltem de 3 ou '
       '6 reais'.format(Sr_Sra, Nome))

print ('_'*70)

print ('o calculo usado para ver o resultado no fim do mes e de: na(numero de apostas)  ga(ganho por aposta)  '
       '"np*gp*30" ')
print('_'*70)

Ga = float(raw_input('Mas voce nao precisa se preocupar com calculos {} {}, apenas me informar: Qual o ganho por aposta'
                     ' que voce quer ter?'.format(Sr_Sra, Nome)))
# o bagulho la de cima o bagulho de eu estar bebado

pa180 = Ga / 180
Rpa80 = pa180 - Ga
pa160 = Ga/60
Rpa60 = pa160 - Ga
pa150 = Ga / 50
Rpa50 = pa150 - Ga
print ('_'*70)
Na = float(raw_input('Agora me informe por favor {} {}, Qual o numero de apostas por dia que quer fazer {}? (lembre-se'
                     ' tente inserir um numero de aposta sempre maior de 50 reais, para maiores lucros)'
                     .format(Sr_Sra, Nome, Sr_Sra)))

Gasto = float(raw_input('Quanto voce deseja gastar por aposta {}'.format(Sr_Sra)))


print ('Otimas Escolhas {}'.format(Sr_Sra))

print ('_'*70)
print ('Seus rendimentos sao: {} reais diarios, {} Reais semanais e {} Reais mensais. Seu gasto diario por aposta '
       'considerando a margem de {} reais sera de {} por dia'
       ' espero ter ajudado {} {} tenha um otimo dia!. Em uma porcentagem 50% de erro seu resultado final vai ser de'
       'em um resultado de 40% de erros seu resultado vai ser de {} e em um resultado com 20% de erro seu resultado vai'
       'ser de {} isso e tudo {} Tenha um bom dia'

       .format(Ga*Na*1, Ga*Na*7, Ga*Na*30, Gasto, Gasto*Na, Sr_Sra, Nome, Rpa80, Rpa60, Rpa50, Sr_Sra))
