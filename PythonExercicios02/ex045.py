#Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

print('''Suas opções:
[  0  ] PEDRA
[  1  ] PAPEL
[  2  ] TESOURA''')

#Lista
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']

#Informa valor inteiro
jogada = int(input('Qual é a sua jogada?'))
computador = randint(0,2)

#Verifica se o jogador digitou um número corretamente.
if jogada not in (0, 1, 2): #Se valor digitado não for 0, 1, 2 ...
    print('Opção inválida. Tente novamente.')
    exit() #Encerra execução

#Contagem
print('JO')
sleep (0.5)
print('KEN')
sleep(0.5)
print('PO')

#Exibe as escolhas
print('='*22)
print(f'Computador jogou {opcoes[computador]}')              #retorna o elemento da lista correspondente ao índice do computador.
print(f'Jogador jogou {opcoes[jogada]}')                              #retorna o elemento da lista correspondente ao índice do jogador.
print('='*22)

#Verifica um vencedor ou empate.
if (jogada == 0 and computador == 2) or (jogada == 1 and computador == 0) or (jogada == 2 and computador == 1):
    print('JOGADOR VENCE')
elif jogada == computador:
    print('EMPATE')
else:
    print('JOGADOR PERDE')



















