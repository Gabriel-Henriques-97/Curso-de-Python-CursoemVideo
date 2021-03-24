# Desafio 36:
'''print('-=-'*11)
print('\tANALISADOR DE EMPRÉSTIMO')
print('-=-'*11)

valcasa = float(input('Digite o valor do imóvel: '))
salario = float(input('Informe o seu salário: '))
ano = float(input('Em quantos anos pretende pagar: '))

mes = ano * 12

prestação = valcasa//mes
print('\nA prestação será de R${:.2f} por mês'.format(prestação))

if prestação > salario*30/100:
    print('\nSua prestação passa de 30% do seu salário. \n>>>Empréstimo negado.<<<')
else:
    print('\n>>>Empréstimo aprovado!<<<')'''

# Desafio 37: Conversão de Bases
'''num = int(input('Digite um número inteiro: '))
print('Escolha uma base para conversão: \n'
      '1 -> Binário\n'
      '2 -> Octal\n'
      '3 -> Hexadecimal')
opção = int(input('Sua opção:  '))

if opção == 1:
      print('{} convertido para binário é {}' .format(num, bin(num)[2:]))
elif opção == 2:
      print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opção == 3:
      print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
      print('Opção inválida! Tente novamente! :/')'''

# Desafio 38:
'''n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 == n2:
    print('{} e {} são iguais'.format(n1, n2))
elif n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
else:
    print('{} é maior que {}'.format(n2, n1))'''

# Desafio 39:
'''from datetime import date
nasci = int(input('Informe seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nasci
alista = 18 - idade

if idade < 18:
    print('Você ainda deverá se alistar. Faltam {} ano(s).'.format(alista))
elif idade == 18:
    print('Você já deve ir se alistar.')
else:
    print('Já passou {} anos seu tempo de alistamento.'.format(-alista))'''

# Desafio 40:
'''n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('Reprovado.')
elif 5.0 <= media <= 6.9:
    print('Recuperação.')
else:
    print('Aprovado.')'''

# Desafio 41:
'''from datetime import date
nasci = int(input('Informe seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nasci

if idade <= 9:
    print('Categoria Mirim.')
elif 9 < idade <= 14:
    print('Categoria Infantil.')
elif 14 < idade <=19:
    print('Caegoria Junior.')
elif 19 < idade <=20:
    print('Categoria Sênior.')
else:
    print('Categoria Master.')'''

# Desafio 42:
'''print('-=-'*10)
print('Analisador de Triângulos')
print('-=-'*10)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo. ')
    if r1 == r2 == r3:
          print('O triângulo é equilátero.')
    elif r1 != r2 != r3 != r1:
          print('O triângulo é escaleno.')
    else:
          print('O triangulo é isósceles')
else:
    print('Os segmentos acima não podem formar triângulo!')'''

# Desafio 43:
'''peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso/(altura**2)
print('Seu IMC é de {:.2f}.'.format(imc))

if imc <= 18.5:
    print('Abaixo do peso.')
elif 18.5 < imc <= 25:
    print('Peso ideal.')
elif 25 < imc <= 30:
    print('Sobrepeso.')
elif 30 < imc <= 40:
    print('Obesidade.')
else:
    print('Obesidade Mórbida.')'''

# Desafio 44:
'''print('{:=^40}'.format(' LOJA GENÉRICA '))
valor = float(input('Insira o valor das compras: '))
formapag = int(input('Digite a forma de pagamento: \n\n'
                     '1 --> À vista no dinheiro ou cheque\n'
                     '2 --> À vista no cartão\n'
                     '3 --> 2x no cartão\n'
                     '4 --> 3x ou mais no cartão\n'))

if formapag == 1:
    total = valor - (valor * 10 / 100)
    print('10% de desconto ')
elif formapag == 2:
    total = valor - (valor * 5 / 100)
    print('5% de desconto. ')
elif formapag == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {:.2f} sem juros'.format(parcela))
elif formapag == 4:
      total = valor + (valor * 20 / 100)
      totparc = int(input('Quantas parcelas? '))
      parcela = total/totparc
      print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totparc, parcela))
else:
      total = 0
      print('Opção inválida de pagamento. Tente novamente.')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(valor, total))'''

# Desafio 45:
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

jog = int(input('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
                '\t\t\tJOKENPO!\n'
                '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'
                'Escolha uma das opções:\n\n'
                '0 --> Pedra\n'
                '1 --> Papel\n'
                '2 --> Tesoura\n'
                'Qual sua escolha? '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)

print('-=' * 15)
print('O computador escolheu {}'.format(itens[pc]))
print('Você jogou {}'.format(itens[jog]))
print('-='* 15)

if pc == 0:
      if jog == 0:
            print('Deu empate! ')
      elif jog == 1:
            print('Parabéns! Você ganhou!')
      elif jog == 2:
            print('O computador ganhou!')
      else:
            print('Opção inválida! Tente novamente.')
elif pc == 1:
      if jog == 0:
            print('O computador ganhou!')
      elif jog == 1:
            print('Deu empate!')
      elif jog == 2:
            print('Parabéns! Você ganhou!')
      else:
            print('Opção Inválida! Tente novamente.')
elif pc == 2:
      if jog == 0:
            print('Parabéns! Você ganhou!')
      elif jog == 1:
            print('O computador ganhou!')
      elif jog == 2:
            print('Deu empate!')
      else:
            print('Opção inválida! Tente novamente.')
else:
      print('Opção inválida! Tente novamente.')
