#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
from colorama import Fore, Back, Style

número = (int(input(Fore.LIGHTMAGENTA_EX + 'Me diga um número qualquer: ' + Style.RESET_ALL)))


if número % 2 ==0: # Se "número" é divisível por 2 (resto 0) = PAR
    print('O número {} '.format(número) + Fore.BLUE + 'PAR' + Style.RESET_ALL)


else:
    print ('O número {} '.format(número) + Fore.BLUE + 'ÍMPAR' + Style.RESET_ALL)