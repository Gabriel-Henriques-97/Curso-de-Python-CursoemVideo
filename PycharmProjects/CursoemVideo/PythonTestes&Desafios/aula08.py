'''import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}' .format(num, raiz))'''

'''import random
num = random.randint(1, 10)
print(num)'''

#Desafio 16:
'''import math
num = float(input('Digite um número real qualquer: '))
print('Sua porção inteira é {}' .format(math.floor(num)))'''

#Desafio 17:
'''import math
co = float(input('Digite comprimento do cateto oposto: '))
ca = float(input('Digite comprimento do cateto adjacente: '))
print('A hipotenusa é {}' .format(math.hypot(co, ca)))'''

#Desafio 18:
'''from math import radians, sin, cos, tan
ang = float(input('Informe um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Seu seno é {:.2f}\n'
      'Seu cosseno é {:.2f}\n'
      'Sua tangente é {:.2f}'
      .format(sen, cos, tan))'''

#Desafio 19:
'''import random
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
alunos = [a1, a2, a3, a4]
escolhido = random.choice(alunos)
print('O aluno sorteado foi: {}' .format(escolhido))'''

#Desafio 20:
'''from random import shuffle
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print('O aluno sorteado foi: {}' .format(alunos))'''

#Desafio 21:
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Penso, Logo Creio (mastered).mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass



