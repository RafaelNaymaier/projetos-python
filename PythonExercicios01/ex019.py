#Um professor que sortear um dos seus quatro alunos para apagar o quadro.
# #Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

#Formas de resolver o mesmo problema

#Forma 01

#from random import choice
#al01 = input('Primeiro aluno: ')
#al02 = input('Segundo aluno: ')
#al03 = input('Terceiro aluno: ')
#al04 = input('Quarto aluno: ')
 #argumentos podem receber apenas uma função

#print ('O aluno escolhido foi {}'.format(choice([al01,al02,al03,al04])))

#Forma 02
#rom random import choice
#al01 = str(input('Primeiro aluno: '))
#al02 = str(input('Segundo aluno: '))
#al03 = str(input('Terceiro aluno: '))
#al04 = str(input('Quarto aluno: '))

#sort = (al01, al02, al03, al04)

#print('O aluno escolhido foi o {}'.format(choice(sort)))

#forma 03
from random import choice
al01 = str(input('Primeiro aluno: '))
al02 = str(input('Segundo aluno: '))
al03 = str(input('Terceiro aluno: '))
al04 = str(input('Quarto aluno: '))

lista = [al01, al02, al03, al04]
escolhido = choice(lista) #retorna valor de lista para escolhido

print('O aluno escolhido foi o {}'.format(escolhido))