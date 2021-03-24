'''frase = 'Curso em Vídeo Python'
print(frase[:14])'''

#Desafio 22:
'''nome = str(input('Digite seu nome completo: ')).strip()
print('Tudo maiúsculo: {}' .format(nome.upper()))
print('Tudo minúsculo: {}' .format(nome.lower()))
print('Total de letras sem os espaços: {}'.format(len(nome) - nome.count(' ')))
print('Nª de letras do primeiro nome: {}' .format(nome.find(' ')))'''

#Desafio 23:
'''num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}' .format(u, d, c, m))'''

#Desafio 24:
'''cid = input('Digite o nome da sua cidade: ').strip()
print(cid[:5].upper() == 'SANTO')'''

#Desafio 25:
'''nome = input('Digite o seu nome completo: ').strip()
print('Seu nome tem Silva? {}' .format('silva' in nome.lower()))'''

#Desafio 26:
'''frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.' .format(frase.count('A')))
print('A primeira letra A apareceu na posição {}' .format(frase.find('A')+1))
print('A última letra A apareceu na posição {}' .format(frase.rfind('A')+1))'''

#Desafio 27:
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é: {}' .format(nome[0]))
print('Seu último nome é: {}' .format(nome[len(nome)-1]))

