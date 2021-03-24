''' for c in range(1,6):
    print('Oi')
print('FIM\n')

for c in range(6,0,-1):
    print(c)
print('FIM\n')

for c in range(0,7,2):
    print(c)
print('FIM\n')

n = int(input("Digite um número: "))
for c in range(0,n):
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n  # s += n
print('O somatório de todos os valores foi {}'.format(s))'''

#######################################################################################################################

# Desafio 46: Countdown Fogos de Artifício
'''from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Fogos lançados!')'''

# Desafio 47: Números pares
'''for c in range (0,51, 2):
    if c % 2 ==0:
        print(c)
print('Fim')'''

# Desafio 48: soma entre todos os números ímpares entre 1 e 500
'''s = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        print(c)
        s = s+c
print('A soma entre os ímpares múltiplos de 3 é {}'.format(s))'''

# Desafio 49: Tabuada
'''n = int(input('Digite um número inteiro: '))
print('Tabuada de {}:'.format(n))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, c * n))'''

# Desafio 50: soma entre pares (digitados pelo usuário)
'''s = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s = s + n  # s += n
print('O somatório de todos os valores pares foi {}'.format(s))'''

# Desafio 51: PA
'''primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1)* razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='-> ')
print('Fim')'''

# Desafio 52: Número primo (/1 e /por ele mesmo)
'''num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vezes'.format(num, total))
if total == 2:
    print('E por isso ele é primo!')
else:
    print(' E por isso ele não é primo!')'''

# Desafio 53:
'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
# inverso = ''
# for letra in range(len(junto) - 1, -1, -1):
#    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')'''

# Desafio 54: Maioridade 7 pessoas
'''from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    nasc = int(input('Digite o ano que a {}ª pessoa nasceu: '.format(pessoa)))
    idade = atual - nasc
    if idade >=21:
        maior = maior + 1
    else:
        menor = menor + 1
print('\nPessoas maiores de idade: {}\nPessoas menores de idade: {}'.format(maior, menor))'''

# Desafio 55: Ler peso 5 pessoas e mostrar o maior e o menor peso lido
'''maior = 0
menor = 0
for p in range(0, 5):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(p + 1)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))'''

# Desafio 56: ler nome, idade e sexo de 4 pessoas
# mostrar média de idade, nome do homem mais velho e qts mulheres < 20 anos
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(0,4):
    print('----- {}ª PESSOA -----'.format(p + 1))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Informe seu sexo [M/F]: '))
    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
