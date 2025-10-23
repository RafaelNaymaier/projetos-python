#Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o osuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu


from random import randint
from time import sleep
from colorama import Style, Fore, Back

linha = '─═─' *12

print(Fore.YELLOW + '{}' .format(linha)+Style.RESET_ALL)
print (Fore.BLUE + 'Vou pensar em um número entre 0 e 5. Tente adivinhar...' + Style.RESET_ALL)
print(Fore.YELLOW + '{}' .format(linha)+Style.RESET_ALL)

num = int(input('Em que número eu pensei? '))
pen = randint(0, 5)
print (pen)

print(Fore.LIGHTMAGENTA_EX + 'PROCESSANDO...' + Style.RESET_ALL)
sleep(2)

if num==pen:
    print(Fore.GREEN + 'PARABÉNS! Você conseguiu me vencer!' + Style.RESET_ALL)

else:
    print(Fore.RED + 'GANHEI! eu pensei no número {} e não no {}'.format(pen, num)+Style.RESET_ALL)
