# lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'  # Nas tuplas, pode ter parênteses ou não
# tuplas sãp imutáveis

'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')'''

# print(sorted(lanche))

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))  # Conta quantas vezes aparece o item
print(c.index(8))  # Diz a posição do item'''

#################################################################################################################

# Desafio 72:
'''numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', \
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
user = int(input('Digite um número entre 0 e 20: '))

while True:
    if 0 <= user <= 20:
        print(f'Você digitou o número {numeros[user]}.')
        break
    else:
        print('Opção inválida, tente de novo. ')
        user = int(input('Digite um número entre 0 e 20: '))'''

# Desafio 73:
'''times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')'''

# Desafio 74:
'''from random import randint
numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)

print(f'Sorteei os números {numeros}') 
print(f'O maior valor foi {max(numeros)} e o menor foi {min(numeros)}')'''

# Desafio 75:
'''a = b = c = d = 0
numeros = (a, b, c, d)
for count in range(0, 4):
    num = int(input('Digite um número: '))

    if numeros == 0:
        a = num in range(0)
        if a == num:
            b = num in range(1)
        elif b == num:
            c = num in range(2)
        elif c == num:
            d = num in range(3)

print(numeros)'''

# Desafio 75: Resposta do curso
'''num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição. ')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')'''

# Desafio 76:
'''produtos = 'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, \
           'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, \
           'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90
print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')

print('-'*40)'''

# Desafio 77:
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
