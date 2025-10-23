#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista.
#A segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from time import sleep
from random import randint



def sorteia(a):
    for c in range(1, 6):
        a.append(randint(0, 10))
    print(f'Sorteando os 5 valores da lista:', end=' ')
    for n in a:
        print(f'{n}', end=' ')
        sleep(0.3)
    print('PRONTO!')

def somapar(a):
    soma = 0
    for n in a:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros} temos {soma}')


#Programa
numeros = list()
sorteia(numeros)
somapar(numeros)











