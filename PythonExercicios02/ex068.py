#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou ano final do jogo

print('-'*35,'\nVAMOS JOGAR PAR OU ÍMPAR\n', '-'*35, sep='')
from random import randint
vezes = 0

#Loop principal
while True:

    #Verifica se as entradas são válidas.
    try:
        valor = int(input('Digite um valor: '))
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        print('-'*35)
    except (ValueError, TypeError, IndexError):
        print('Resposta inválida. Tente novamente.')
        continue
    if escolha != 'P' and escolha != 'I':
        continue

    #Computador gera um número de 0 a 10.
    computador = randint(0,10)

    #Verifica se a soma é PAR ou ÍMPAR.
    soma = valor + computador
    if soma % 2 == 0:
        par_ou_impar = 'PAR'
    else:
        par_ou_impar = 'ÍMPAR'

    #Informa o resultado.
    print(f'Você jogou {valor} e o computador {computador}. total de {soma} deu {par_ou_impar}')
    print('-'*35)

    #Informa se o usuário ganhou ou perdeu.
    if escolha == 'P' and par_ou_impar == 'PAR' or escolha == 'I' and par_ou_impar == 'ÍMPAR':
        print('Você Ganhou!')
        vezes += 1
        print('Vamos jogar novamente...')
        print('-'*35)
    else:
        print('Você Perdeu!')
        print('-'*35)
        break

print(f'GAME OVER! você venceu {vezes} vezes!')

