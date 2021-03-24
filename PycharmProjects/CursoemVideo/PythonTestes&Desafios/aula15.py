"""nome = 'José'
idade = 33
salario = 987.30
print(f'O {nome} tem {idade} e ganha R${salario:.2f}')"""  # f strings

##############################################################################################################

# Desafio 66:
'''soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')'''

# Desafio 67:
'''n = 0
cont = 1
while True:
    n = int(input('Digite um número inteiro positivo [Negativo sai do programa]: '))

    if n >= 0:
        print(f'Tabuada de {n}')
        for c in range(1, 11):
            print('{} x {} = {}'.format(n, c, c * n))
    else:
        print('O programa será encerrado.')
        break'''

# Desafio 68:
'''from random import randint
vitorias = 0
while True:
    pc = randint(0, 10)
    print('-='*30)
    jog = int(input('Digite um número: '))
    opc = str(input('Escolha par ou ímpar [P/I]: ')).strip().upper()[0]
    print('-='*30)
    if opc == 'P':
        if (jog + pc) % 2 == 0:
            print('Deu par. Você venceu! Parabéns! ')
            vitorias += 1
        else:
            print('Deu ímpar. Você perdeu. Tente novamente. ')
            break
    elif opc == 'I':
        if (jog + pc) % 2 != 0:
            print('Deu ímpar. Você venceu! Parabéns! ')
            vitorias += 1
        else:
            print('Deu par. Você perdeu. Tente novamente. ')
            break
    else:
        print('Opção inválida! Tente de novo. ')

print(f'Você venceu {vitorias} vezes. ')'''

# Desafio 69:
'''idade = sexo = maior18 = homem = mulher = opc = 0
while True:
    print('-='*30)
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]

    if sexo == 'M':
        homem += 1
        maior18 += 1
    elif sexo == 'F' and idade < 18:
        mulher += 1
    elif sexo == 'F' and idade > 18:
        maior18 += 1
    else:
        sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
    opc = str(input('Deseja cadastrar mais uma pessoa? [S/N] ')).strip().upper()[0]

    if opc == 'S':
        print('-=' * 30)
        idade = int(input('Qual a sua idade? '))
        sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]

        if sexo == 'M':
            homem += 1
            maior18 += 1
        elif sexo == 'F' and idade < 18:
            mulher += 1
        elif sexo == 'F' and idade > 18:
            maior18 += 1
        else:
            sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
        opc = str(input('Deseja cadastrar mais uma pessoa? [S/N] ')).strip().upper()[0]

    if opc == 'N':
        print('-='*30)
        print(f'O total de pessoas com mais de 18 anos é de {maior18}.')
        print(f'Foram registrados {homem} homens.')
        print(f'Foram registradas {mulher} mulheres menores de 18 anos.')
        break
    else:
        print('Opção inválida. Tente novamente. ')
        opc = str(input('Deseja cadastrar mais uma pessoa? [S/N] ')).strip().upper()[0]'''

# Desafio 69: Resposta do curso
'''tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')'''

# Desafio 70:
'''total = totmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total = total + preco

    if preco > 1000:
        totmil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper() [0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do Programa'))
print(f'O total das compras foi de {total}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')'''

# Desafio 71: 50, 20, 10, 1
print('='*30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('='*30)

valor = int(input('Informe o valor a ser sacado: R$'))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0

        if total == 0:
            break
print('='*30)
print('Volte sempre! Tenha um bom dia!')
