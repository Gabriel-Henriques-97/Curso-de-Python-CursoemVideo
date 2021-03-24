#ver sobre módulo colorize
#print('\033[1;31;43mOlá, Mundo!\033[m')

'''a = 3
b = 5
print('Os valores são \033[34m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))'''


'''nome = 'Gabriel'
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))'''


nome = 'Gabriel'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;37;40m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['pretoebranco'], nome, cores['limpa']))
