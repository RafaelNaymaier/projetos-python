#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

sorteado = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

#É melhor usar a função.join quando precisar dela novamente no futuro (criar uma variável)
sorteado_formatado = ', '.join(str(n)for n in sorteado)

maior = max(sorteado)
menor = min(sorteado)

'''print('Os valores sorteados foram: ', end='')
for n in sorteado:
    print(f'{n} ', end='')'''

print('Sorteei os valores: ', sorteado_formatado)

''''*' Funciona como desempacotador
print('Os valores sorteados foram:', *sorteado, sep=', ')'''

print(f'\nO maior valor sorteado foi {maior}')

print(f'O menor valor sorteado foi {menor}')





















