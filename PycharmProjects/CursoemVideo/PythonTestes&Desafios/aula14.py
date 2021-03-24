'''for c in range(1, 10):
    print(c)
print('Fim')'''

'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')'''

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''

'''n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares. '.format(par, impar))'''

##################################################################################################################

# Desafio 57:
'''s = 1
while s != 'M' and s != 'F':
    s = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
    if s == 'M':
        print('Seu sexo é masculino. ')
    elif s == 'F':
        print('Seu sexo é feminino. ')
    else:
        print('Informação incorreta. Tente novamente. ')
print('Fim')'''

# Desafio 57: Resposta do curso:
'''sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, insira seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))'''

# Desafio 58:
'''import random
numpc = random.randint(0, 10)
numuser = 11
tentativa = 1

while numuser != numpc:
    numuser = int(input('Tente adivinhar o número escolhido pelo computador entre 0 e 10: '))
    if numuser == numpc:
        print('Parabéns, você acertou!\n'
              'Você precisou de {} tentativas para acertar! '.format(tentativa))
    else:
        tentativa += 1
        if numuser < numpc:
            print('Mais... Tente novamente. ')
        elif numuser > numpc:
            print('Menos... Tente novamente. ')'''

# Desafio 59:
'''
# val1 = int(input('Insira o primeiro valor: '))
# val2 = int(input('Insira o segundo valor: '))
opção = 0
resultado = 0

while opção != 5:
    opção = int(input('Escolha uma opção: \n'
                      '[1] --> Somar\n'
                      '[2] --> Multiplicar\n'
                      '[3] --> Maior número\n'
                      '[4] --> Novos números\n'
                      '[5] --> Sair do programa\n'))
    # val1 = int(input('Insira o primeiro valor: '))
    # val2 = int(input('Insira o segundo valor: '))
    if opção == 1:
        resultado = val1 + val2
        print('Resultado: {}'.format(resultado))
    elif opção == 2:
        resultado = val1 * val2
        print('Resultado: {}'.format(resultado))
    elif opção == 3:
        if val1 > val2:
            print('{} é maior que {}'.format(val1, val2))
        else:
            print('{} é maior que {}'.format(val2, val1))
    elif opção == 4:
        print('Escolha novos números: \n')
        val1 = int(input('Insira o primeiro valor: '))
        val2 = int(input('Insira o segundo valor: '))
    elif opção == 5:
        print('O programa será encerrado. ')
        break
    else:
        print('Opção inválida! ')'''

# Desafio 60:
'''num = int(input('Insira um inteiro: '))
fat = 1
while num != 0:
    fat = fat * num
    num = num - 1
print('O fatorial de {} é {}'.format(num, fat)) '''

# Desafio 60: Resposta 1 do curso
'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''

# Desafio 60: Resposta 2 do curso
'''n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! '.format(n))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''

# Desafio 61:
'''print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('Fim')'''

# Desafio 62:
'''print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados. '.format(total))'''

# Desafio 63:
#  num = int(input('Insira um número: '))
'''anterior = 0
proximo = 0
while proximo < 50:
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior

    if proximo == 0:
        proximo += 1'''

# Desafio 63: Resposta do curso
'''print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {} '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('\nFim')'''

# Desafio 64:
'''num = qtd = soma = 0
while num != 999:
    num = int(input('Digite um valor [999 para parar]: '))
    if num != 999:
        qtd = qtd + 1
        soma = soma + num
print('A quantidade de números digitados foi {} e a soma deles é {}'.format(qtd, soma))'''

# Desafio 65:
num = soma = media = qtd = opc = maior = menor = 0
while opc != 'N':
    num = int(input('Digite um valor: '))
    soma = soma + num
    qtd += 1
    opc = str(input('Deseja continuar? [S/N] ')).upper()

    if opc == 'N':
        media = soma / qtd
        print('A média dos valores lidos foi {}'.format(media))

# para avaliar qual maior número:
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))




