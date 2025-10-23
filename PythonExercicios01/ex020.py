#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# #Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle
al01 = str(input('Primeiro aluno: '))
al02 = str(input('Segundo aluno: '))
al03 = str(input('Terceiro aluno: '))
al04 = str(input('Quarto aluno: '))
lista = [al01, al02, al03, al04]

shuffle(lista)
#escolhido = shuffle(lista) #não funciona pois shuffle não retorna valor a escolhido, apenas o conteúdo interno

print ('A ordem de apresentação será')
print ('{}'.format(lista))