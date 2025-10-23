#Exercício Python 098:
#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
#Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, a cada 1
#b) de 10 até 0, a cada 2
#c) uma contagem personalizada
from time import sleep

def linha():
    print('-'*30)

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo > 0:
        for c in range(inicio, fim+1, passo):
            print(c, end=' ')
            sleep(0.3)
    else:
        for c in range(inicio, fim-1, passo):
            print(c, end=' ')
            sleep(0.3)
    print('FIM')
    linha()

#Programa principal
linha()
contador(1, 10, 1)

contador(10, 0, -2)

print(f'Agora é a sua vez de personalizar a contagem!')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i,f,p)
















