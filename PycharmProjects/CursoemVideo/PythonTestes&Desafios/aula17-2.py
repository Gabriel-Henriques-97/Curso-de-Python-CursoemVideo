"""teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)"""

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

'''galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')'''

##############################################################################################################

# Desafio 84:
'''pessoas = list()
info = list()
qtd = pesado = leve = opc = 0
while True:
    info.append(str(input('Nome: ')))
    qtd += 1
    info.append(float(input('Peso: ')))
    pessoas.append(info[:])
    info.clear()

    if info[1] >= 100:
        pesado += 1
    else:
        leve += 1

    opc = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if opc == 'n':
        break
    if opc != 's':
        print('Opção inválida. Tente de novo. ')


print(f'Foram cadastradas {qtd} pessoas.')
# print(f'O maior peso foi de {(pessoas[1])}Kg. Peso de ')
# print(f'o menor peso foi de {(pessoas[1])}kg. Peso de ')
print(pessoas)'''

# Desafio 84: resposta do curso
'''temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()'''

# Desafio 85:
'''numeros = list()
pares = list()
impares = list()
num = 0
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

numeros.append(pares[:])
numeros.append(impares[:])

print('-='*20)
print(f'Lista dos pares: {sorted(numeros[0])}')
print(f'Lista dos ímpares: {sorted(numeros[1])}')
print('-='*20)'''

# Desafio 85: Resposta do curso
'''num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares foram: {num[0]}')
print(f'Os valores ímpares foram: {num[1]}')'''


# Desafio 86:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for para colocar os valores na matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
# for para ajeitar os dados na tela
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

# Desafio 87:
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
# for para colocar os valores na matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
# for para ajeitar os dados na tela
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')'''


# Desafio 88:









