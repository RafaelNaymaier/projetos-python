#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def linha():
    print('-' * 50)


def maior(*num):
    print(f'Analisando os valores passados...')
    if len(num) == 0:
        print(f'foram informados 0 valores ao todo.')
        print(f'O maior valor informado foi 0')
    else:
        for n in num:
            print(n, end=' ')
            sleep(0.3)
        print(f'foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}')
    linha()


#Programa principal
linha()
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()




























