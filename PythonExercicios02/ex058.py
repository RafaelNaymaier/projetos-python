#Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinha até acertar, mostrando no final quantos palpites foram necessário para vencer.

from random import randint

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10...')
print('Será que você consegue adivinhar qual foi? ')

num_palpites = 0
computador = randint(0, 10)

acertou = False
while not acertou:
    palpite = int(input('Qual é o seu palpite? '))
    num_palpites += 1
    if palpite == computador:
        print(f'Acertou com {num_palpites} tentativas. Parabens!')
        acertou = True
    if palpite < computador:
        print('Mais... Tente mais uma vez.')
    if palpite > computador:
        print('Menos... Tente mais uma vez.')




















