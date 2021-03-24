'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número. ')

# num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos. ')'''

###########################

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)'''
'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')
print('Fim')'''

################################

'''a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''

##############################################################################################################

# Desafio 78:
'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(f'O maior valor foi de {max(valores)} e o menor foi de {min(valores)}')
print(f'O maior valor está na posição {valores.index(max(valores))} '
      f'e o menor na posição {valores.index(min(valores))}')'''

# Desafio 78: Resposta do curso
'''listanum = []
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i} ... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i} ... ', end='')
print()'''

# Desafio 79:
'''numeros = list()
opc = 0
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso! ', end='')
    else:
        print('Valor duplicado. Não vou adicionar. ', end='')

    opc = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if opc == 'n':
        break
    if opc != 's':
        print('Opção inválida. Tente de novo. ')

print(f'Os valores cadastrados foram {sorted(numeros)}')'''

# Desafio 80:
'''lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados foram {lista}')'''


# Desafio 81:
'''numeros = list()
opc = qtd = 0
while True:
    numeros.append(int(input('Digite um valor: ')))
    qtd += 1
    opc = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if opc == 'n':
        break
    if opc != 's':
        print('Opção inválida. Tente de novo. ')

print(f'O total de números digitados foi de {qtd}')
numeros.sort(reverse=True)
print(f'Os valores cadastrados foram {numeros}')

if 5 in numeros:
    print(f'O valor 5 foi digitado e está na {numeros.index(5)} posição.')
else:
    print('O valor 5 não foi digitado e não está na lista.')'''

# Desafio 82:
'''numeros = pares = impares = list()
opc = qtd = 0
while True:
    numeros.append(int(input('Digite um valor: ')))
    qtd += 1
    opc = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if opc == 'n':
        break
    if opc != 's':
        print('Opção inválida. Tente de novo. ')
print('-='*15)
print(f'Primeira lista: {numeros}')

print('Lista dos pares: ', end='')
for pares in numeros:
    if pares % 2 == 0:
        print(pares, end=' ')

print('\nLista dos ímpares: ', end='')
for impares in numeros:
    if impares % 2 != 0:
        print(impares, end=' ')
print('')
print('-='*15)'''

# Desafio 83:
expre = str(input('Digite a expressão: '))
pilha = []
for simb in expre:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida. ')
else:
    print('Sua expressão está errada. ')





