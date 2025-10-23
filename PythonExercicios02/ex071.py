#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.

print(f'{'='*30} \n{'BANCO CEV'.center(30)} \n{'='*30}')

cedula_50 = cedula_20 = cedula_10 = cedula_1 = 0

valor = int(input('Que valor você quer sacar? R$'))

while valor >= 50:
    valor -= 50
    cedula_50 += 1

while valor >= 20:
    valor -= 20
    cedula_20 += 1

while valor >= 10:
    valor -= 10
    cedula_10 += 1

while valor >= 1:
    valor -= 1
    cedula_1 += 1

if cedula_50 > 0:
    print(f'Total de {cedula_50} cédulas de R$50')
if cedula_20 > 0:
    print(f'Total de {cedula_20} cédulas de R$20')
if cedula_10 > 0:
    print(f'Total de {cedula_10} cédulas de R$10')
if cedula_1 > 0:
    print(f'Total de {cedula_1} cédulas de R$1')

print(f'{'='*30} \n{'Volte sempre ao BANCO CEV! Tenha um bom dia!'}')





























