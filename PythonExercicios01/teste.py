

#Cores

'''Códigos de estilo (modificadores):
0 - Reset / Normal
1 - Negrito
4 - Sublinhado
7 - Negativo (inverte texto e fundo)

Códigos de cor (texto):
30 - Preto
31 - Vermelho
32 - Verde
33 - Amarelo
34 - Azul
35 - Magenta
36 - Ciano
37 - Branco

Códigos de cor (fundo):
40 - Preto
41 - Vermelho
42 - Verde
43 - Amarelo
44 - Azul
45 - Magenta
46 - Ciano
47 - Branco

Como usar:
python
# Texto vermelho negrito
print('\033[1;31mTexto vermelho negrito\033[0m')

# Texto amarelo com fundo azul
print('\033[33;44mAmarelo sobre azul\033[0m')

# Texto sublinhado verde
print('\033[4;32mVerde sublinhado\033[0m')'''

import colorama

#print ('\033[31;43mOlá, Mundo! ') #Fonte vermelha, Fundo laranja

'''a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{} \033[m!!!'.format(a, b))'''

'''nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer! {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))'''


nome = 'Guanabara'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer! {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))





