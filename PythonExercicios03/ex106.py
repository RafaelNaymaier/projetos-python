#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
#O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

from time import sleep


def linha(msg, cor):
    tam = len(msg) + 4
    print(f'{cor}~' * tam)
    print(f'{cor}  {msg}')
    print(f'{cor}~' * tam)
    print('\033[0m', end='')



while True:
    linha('SISTEMA DE AJUDA PyHELP', '\033[43m')
    user = input('Função ou biblioteca: ').strip().lower()


    if user == 'fim':
        linha('ATÉ LOGO', '\033[41m')
        break

    linha(f'Acessando o manual do comando {user}', '\033[44m')
    sleep(0.7)
    print('\033[30;47m', end='')
    help(user)
    print('\033[0m', end='')
























