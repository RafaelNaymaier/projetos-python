#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


#valor % 4 ==0

num = int(input('Digite um número: '))

vezes = 0

for c in range (1, num+1):
    if num % c == 0:
        vezes += 1
        print(f'\033[33m{c}\033[m', end=' ')
    else:
        print(f'\033[31m{c}\033[m', end=' ')

print(f'\nO número {num} foi divisível {vezes} vezes')

if vezes == 2:
    print('E por isso ele É PRIMO')

else:
    print ('E por isso ele NÃO É PRIMO')














