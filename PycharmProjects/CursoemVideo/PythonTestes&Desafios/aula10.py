'''nome = str(input('Qual é o seu nome? '))
if nome == 'Gabriel':
    print('Que nome lindo vc tem!')
else:
    print('Seu nome é tão normal... ¬.¬')
print('Bom dia, {}!' .format(nome))'''

'''n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}' .format(m))
#print('Parabéns!' if m>=6 else 'Estude mais!')
if m>=6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')'''

#Desafio 28
'''import random
numpc = random.randint(0, 5)
numuser = int(input('Tente adivinhar o número escolhido pelo computador entre 0 e 5! '))
if numuser == numpc:
    print('Parabéns, você acertou!')
else:
    print('Tente novamente! :/')'''

#Desafio 29:
'''vel = int(input('Qual a velocidade do carro em Km/h? '))
multa = (vel-80)*7
if vel > 80:
    print('Você foi multado e devará pagar {} de multa!' .format(multa))
else:
    print('Tudo tranquilo.')'''

#Desafio 30:
'''num = int(input('Digite um número inteiro: '))
if num%2 == 0:
    print('Seu número é par!')
else:
    print('Seu número é ímpar!')'''

#Desafio 31:
'''dist = float(input('Qual é a distância da sua viagem em Km? '))
if dist <= 200:
    print('Você deverá pagar R${}' .format(dist*0.5))
else:
    print('Você deverá pagar R${}' .format(dist*0.45))'''

#Desafio 32: Ano Bissexto
#import datetime
'''from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))'''


#Desafio 33:
'''n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 < n2:
    maior = n3

print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))'''

#Desafio 34:
'''salario = float(input('Digite o salário: R$'))
if salario > 1250:
    print('Seu novo salário é: {}' .format(salario + (salario*10/100)))
else:
    print('Seu novo salário é: {}' .format(salario + (salario*15/100)))'''

#Desafio 35:
print('-=-'*10)
print('Analisador de Triângulos')
print('-=-'*10)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulo!')
else:
    print('Os segmentos acima não podem formar triângulo!')

